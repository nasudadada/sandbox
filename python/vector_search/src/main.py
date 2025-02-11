import sqlite3
import sqlite_vss
import numpy as np
from openai import OpenAI
import os
from typing import List
import traceback
from datetime import datetime

def generate_embedding(text: str) -> List[float]:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = client.embeddings.create(
        model="text-embedding-3-large",
        input=text.replace('\n', ' ')
    )
    return response.data[0].embedding

def serialize(vector: List[float]) -> bytes:
    return np.asarray(vector).astype(np.float32).tobytes()

def init_db():
    conn = sqlite3.connect('vector_sample.sqlite3')
    conn.enable_load_extension(True)
    
    try:
        # 拡張機能のロードを確認
        sqlite_vss.load(conn)
        vss_version = conn.execute('select vss_version()').fetchone()[0]
        print('SQLite VSS Version: %s' % vss_version)
        
        # メインテーブルを作成
        conn.execute('''
            CREATE TABLE documents(
                id INTEGER PRIMARY KEY,
                title TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # VSS用のテーブルを作成
        conn.execute('''
            CREATE VIRTUAL TABLE IF NOT EXISTS embeddings USING vss0(
                summary_embedding(3072)
            )
        ''')
        
        return conn
        
    except Exception as e:
        print(f"データベース初期化エラー: {e}")
        traceback.print_exc()
        return None

def add_document(conn, title: str):
    try:
        current_time = datetime.now()
        
        # まずdocumentsテーブルに追加
        conn.execute('''
            INSERT INTO documents(title, created_at)
            VALUES (?, ?)
        ''', (title, current_time))
        
        # 追加したレコードのIDを取得
        last_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
        
        # titleからembeddingを生成
        embedding = generate_embedding(title)
        
        # embeddingsテーブルに追加（rowidを明示的に指定）
        conn.execute(
            'INSERT INTO embeddings(rowid, summary_embedding) VALUES (?, ?)',
            (last_id, serialize(embedding))
        )
        conn.commit()
        
    except Exception as e:
        print(f"ドキュメント追加エラー: {e}")
        traceback.print_exc()

def search_similar(conn, query: str, top_k=5):
    try:
        query_embedding = generate_embedding(query)
        
        cursor = conn.execute('''
            SELECT 
                d.title,
                e.distance
            FROM embeddings e
            JOIN documents d ON e.rowid = d.id
            WHERE vss_search(e.summary_embedding, vss_search_params(?, 5))
            ORDER BY e.distance
            LIMIT ?
        ''', (serialize(query_embedding), top_k))
        
        results = cursor.fetchall()
        print(f"Raw results: {results}")
        
        return results
        
    except Exception as e:
        print(f"検索エラー: {e}")
        traceback.print_exc()
        return []

def main():
    conn = init_db()
    if conn is None:
        print("データベース接続に失敗しました")
        return

    try:
        # ジャンルデータ
        genres = [
            "野球",
            "サッカー",
            "バスケットボール"
        ]
        
        for genre in genres:
            add_document(conn, genre)
        print(f"ジャンル {len(genres)} 件の追加成功\n")

        # テストするワード一覧
        test_queries = [
            "阪神タイガース",
            "読売ジャイアンツ",
            "鹿島アントラーズ",
            "浦和レッズ",
            "千葉ジェッツ",
            "横浜ビー・コルセアーズ"
        ]

        # 各ワードについて類似度を確認
        for query in test_queries:
            print(f"\n検索ワード: {query}")
            print("-" * 50)
            
            results = search_similar(conn, query)
            print(f"生の検索結果: {results}") 
            
            for title, distance in results:
                print(f"ジャンル: {title}")
                print(f"距離: {distance}")

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        traceback.print_exc()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()