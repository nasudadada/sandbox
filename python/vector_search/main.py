from transformers import AutoTokenizer, AutoModel
import torch
import chromadb
from chromadb.config import Settings

# 日本語BERTモデルをロード
model_name = "cl-tohoku/bert-base-japanese-whole-word-masking"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# ChromaDBクライアントを初期化
client = chromadb.Client(Settings(persist_directory="./chroma_db"))

# コレクションを作成または取得
collection = client.get_or_create_collection("my_collection")

# テキストをembeddingし、保存する関数
def embed_and_store(texts, ids):
    embeddings = []
    for text in texts:
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        embeddings.append(outputs.last_hidden_state.mean(dim=1).squeeze().numpy())
    
    collection.add(
        embeddings=[e.tolist() for e in embeddings],
        documents=texts,
        ids=ids
    )

texts = ["プロ野球（巨人）", "プロ野球（阪神）", "プロ野球（広島）", "Jリーグ（川崎フロンターレ）", "Jリーグ（横浜FC）", "Jリーグ（FC東京）"]
ids = ["id1", "id2", "id3", "id4", "id5", "id6"]

embed_and_store(texts, ids)

# 保存されたデータを検索する
query = "Jリーグ（横浜FC） i"
query_inputs = tokenizer(query, return_tensors="pt", padding=True, truncation=True, max_length=512)
with torch.no_grad():
    query_outputs = model(**query_inputs)
query_embedding = query_outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=2
)

print(f"query: {query}")
print(f"results: {results}")
