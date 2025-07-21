# Rust Zero 学習プロジェクト

このリポジトリは、[ゼロから学ぶRust システムプログラミングの基礎から線形型システムまで](https://www.kodansha.co.jp/book/products/0000371815) の書籍に沿ってRust言語を学習するためのプロジェクト。

## 開発環境

このプロジェクトはDocker + devcontainerを使用して、macOSでも書籍と同じUbuntu環境で学習できるように設定されています。

### 必要なソフトウェア

- Docker Desktop
- Visual Studio Code
- VS Code Extension: "Remote - Containers"

### セットアップ手順

1. リポジトリをクローン
```bash
git clone <repository-url>
cd rust_zero
```

2. 開発環境を起動
```bash
./scripts/dev.sh start
```

3. VS Codeでプロジェクトを開く

4. VS Codeで `Cmd+Shift+P` を押して "Remote-Containers: Reopen in Container" を実行

5. コンテナ内で開発開始！

### 便利なコマンド

```bash
# 開発環境の起動
./scripts/dev.sh start

# 開発環境の停止
./scripts/dev.sh stop

# 開発環境の再起動
./scripts/dev.sh restart

# ログの確認
./scripts/dev.sh logs

# コンテナ内でシェルを起動
./scripts/dev.sh shell

# コンテナの再ビルド
./scripts/dev.sh build

# キャッシュのクリア
./scripts/dev.sh clean
```

## 参考資料

- [Rust Zero GitHub](https://github.com/ytakano/rust_zero)

