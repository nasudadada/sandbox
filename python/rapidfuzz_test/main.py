from rapidfuzz import fuzz, process
import re
import unicodedata
from typing import Optional, Tuple

def preprocess_name(name: str) -> str:
    """
    名前の前処理を行います
    """
    # 全角を半角に変換
    name = unicodedata.normalize('NFKC', name)
    
    # マスタとなる表記揺れ辞書
    name_master = {
        # アイドルグループ
        '乃木坂46': ['乃木坂', 'のぎざか', 'ノギザカ', 'のぎ坂'],
        'AKB48': ['AKB', 'エーケービー', 'えーけーびー'],
        '櫻坂46': ['さくら坂', 'サクラザカ', '桜坂'],
        '日向坂46': ['ひなた坂', 'ヒナタザカ'],
        
        # ジャニーズ系
        'King & Prince': ['キングアンドプリンス', 'きんぷり'],
        'Snow Man': ['スノーマン', 'すのーまん'],
        'SixTONES': ['ストーンズ', 'ストンズ', 'シックストーンズ'],
        'なにわ男子': ['なにわだんし', 'ナニワダンシ']
    }
    
    # 表記揺れマスタから検索
    for master_name, variations in name_master.items():
        if name.lower() in [v.lower() for v in variations + [master_name]]:
            return master_name
    
    # 記号類を空白に置換
    name = re.sub(r'[・.．\-\_\(\)（）&＆]', ' ', name)
    
    # 数字を除去
    name = re.sub(r'\d+', '', name)
    
    # 余分な空白を削除してトリム
    return ' '.join(name.split()).strip()

def calculate_similarity(x: str, y: str, score_cutoff: float = 0) -> float:
    """
    2つの文字列の類似度を計算します
    """
    return max(
        fuzz.token_set_ratio(x, y, score_cutoff=score_cutoff),
        fuzz.partial_ratio(x.lower(), y.lower(), score_cutoff=score_cutoff)
    )

def find_best_match(search_term: str, master_list: list[str], threshold: float = 60.0) -> Optional[Tuple[str, float]]:
    """
    検索ワードに最も類似するグループ名を返します
    
    Args:
        search_term: 検索ワード
        master_list: グループマスタのリスト
        threshold: マッチングの閾値（0-100）
    
    Returns:
        Tuple[str, float]: (マッチしたグループ名, 類似度) または None
    """
    # extractOneを使用して最適なマッチを取得
    result = process.extractOne(
        search_term,
        master_list,
        scorer=calculate_similarity,
        processor=preprocess_name,
        score_cutoff=threshold
    )
    
    if result:
        return (result[0], result[1])  # 名前と類似度のみを返す
    return None

def main():
    # グループ（マスタ情報）のサンプル
    performer_master = [
        "乃木坂46",
        "櫻坂46",
        "日向坂46",
        "AKB48",
        "King & Prince",
        "Snow Man",
        "なにわ男子",
        "SixTONES",
        "ストーンズ"
    ]
    
    # クエリのサンプル
    search_terms = [
        "乃木坂",
        "のぎざか46",
        "ノギザ",
        "キングアンドプリンス",
        "キンプリ",
        "スノーマン",
        "ストーンズ",
        "存在しない"
    ]
    
    print("=== 検索結果 ===")
    for term in search_terms:
        result = find_best_match(term, performer_master)
        if result:
            matched_name, similarity = result
            print(f"\n検索ワード: {term}")
            print(f"マッチしたグループ: {matched_name}")
            print(f"類似度: {similarity:.1f}%")
        else:
            print(f"\n検索ワード: {term}")
            print("マッチするグループが見つかりませんでした")

if __name__ == "__main__":
    main()
