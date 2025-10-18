# Docker + devcontainer で Rust Zero 学習環境を構築

## 概要

[Rust Zero](https://www.kodansha.co.jp/book/products/0000371815) の書籍は WSL の Ubuntu を想定していますが、macOS でも Docker + devcontainer を使うことで同じ環境で学習できます。

## 作成したファイル構成

```
rust_zero/
├── Dockerfile                    # Ubuntu + Rust 環境の定義
├── docker-compose.yml           # コンテナ管理設定
├── .dockerignore                # Docker ビルド時の除外ファイル
├── .devcontainer/
│   └── devcontainer.json        # VS Code devcontainer 設定
├── scripts/
│   └── dev.sh                   # 開発環境管理スクリプト
├── docs/
│   └── docker-devcontainer-setup.md  # このファイル
└── README.md                    # プロジェクト概要
```

## 各ファイルの詳細

### 1. Dockerfile

Ubuntu 22.04 ベースの Rust 開発環境を定義：

```dockerfile
FROM ubuntu:22.04

# 環境変数の設定
ENV DEBIAN_FRONTEND=noninteractive
ENV RUSTUP_HOME=/usr/local/rustup
ENV CARGO_HOME=/usr/local/cargo
ENV PATH=/usr/local/cargo/bin:$PATH

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    pkg-config \
    libssl-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Rustのインストール
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && source $HOME/.cargo/env \
    && rustup default stable \
    && rustup component add rust-src rust-analyzer

WORKDIR /workspace
CMD ["/bin/bash"]
```

**ポイント：**
- `source $HOME/.cargo/env` で書籍と同じ手順を再現
- `rust-src` と `rust-analyzer` を追加でインストール（IDE サポート用）

### 2. docker-compose.yml

開発環境の管理とボリュームマウントを設定：

```yaml
version: '3.8'

services:
  rust-dev:
    build: .
    container_name: rust-zero-dev
    volumes:
      - .:/workspace
      - cargo-cache:/usr/local/cargo/registry
      - target-cache:/workspace/target
    working_dir: /workspace
    stdin_open: true
    tty: true
    environment:
      - RUST_BACKTRACE=1
    ports:
      - "8080:8080"

volumes:
  cargo-cache:
  target-cache:
```

**ポイント：**
- `cargo-cache` と `target-cache` でビルド時間を短縮
- `stdin_open: true` と `tty: true` で対話的な操作を可能に

### 3. .devcontainer/devcontainer.json

VS Code でコンテナ内開発を可能にする設定：

```json
{
  "name": "Rust Zero Development",
  "dockerComposeFile": "../docker-compose.yml",
  "service": "rust-dev",
  "workspaceFolder": "/workspace",
  
  "customizations": {
    "vscode": {
      "extensions": [
        "rust-lang.rust-analyzer",
        "tamasfe.even-better-toml",
        "serayuzgur.crates",
        "vadimcn.vscode-lldb",
        "ms-vscode.vscode-json"
      ],
      "settings": {
        "rust-analyzer.checkOnSave.command": "clippy",
        "rust-analyzer.cargo.buildScripts.enable": true,
        "rust-analyzer.procMacro.enable": true,
        "rust-analyzer.lens.enable": true,
        "rust-analyzer.lens.implementations.enable": true,
        "rust-analyzer.lens.references.adt.enable": true,
        "rust-analyzer.lens.references.trait.enable": true,
        "rust-analyzer.lens.references.enumVariant.enable": true,
        "rust-analyzer.lens.references.method.enable": true
      }
    }
  },

  "forwardPorts": [8080],
  "postCreateCommand": "rustc --version && cargo --version",
  
  "remoteUser": "root"
}
```

**ポイント：**
- Rust 開発に必要な拡張機能を自動インストール
- `rust-analyzer` の設定を最適化
- `postCreateCommand` で環境確認を自動実行

### 4. scripts/dev.sh

開発環境の管理を簡単にするスクリプト：

```bash
#!/bin/bash

case "$1" in
    "start")
        echo "🚀 Rust Zero 開発環境を起動中..."
        docker-compose up -d
        echo "✅ 開発環境が起動しました"
        echo "📝 VS Codeで 'Reopen in Container' を実行してください"
        ;;
    "stop")
        echo "🛑 Rust Zero 開発環境を停止中..."
        docker-compose down
        echo "✅ 開発環境が停止しました"
        ;;
    # ... その他のコマンド
esac
```

## セットアップ手順

### 1. 必要なソフトウェア

- Docker Desktop
- Visual Studio Code
- VS Code Extension: "Remote - Containers"

### 2. 環境構築

```bash
# 1. リポジトリをクローン
git clone <repository-url>
cd rust_zero

# 2. スクリプトに実行権限を付与
chmod +x scripts/dev.sh

# 3. 開発環境を起動
./scripts/dev.sh start

# 4. VS Codeでプロジェクトを開く

# 5. VS Codeで Cmd+Shift+P → "Remote-Containers: Reopen in Container"
```

### 3. 便利なコマンド

```bash
./scripts/dev.sh start   # 開発環境起動
./scripts/dev.sh stop    # 開発環境停止
./scripts/dev.sh restart # 開発環境再起動
./scripts/dev.sh logs    # ログ確認
./scripts/dev.sh shell   # コンテナ内でシェル起動
./scripts/dev.sh build   # コンテナ再ビルド
./scripts/dev.sh clean   # キャッシュクリア
```

## 書籍との違い

### 書籍の想定環境
- WSL Ubuntu
- 手動での Rust インストール
- `source $HOME/.cargo/env` での環境変数設定

### 今回の環境
- Docker Ubuntu 22.04
- 自動化された Rust インストール
- 同じ `source $HOME/.cargo/env` を使用
- VS Code devcontainer による統合開発環境

## メリット

1. **環境の再現性** - 誰でも同じ環境を構築可能
2. **macOS 対応** - WSL が不要
3. **VS Code 統合** - rust-analyzer などの拡張機能が自動設定
4. **キャッシュ機能** - ビルド時間の短縮
5. **簡単な管理** - スクリプトで環境の起動・停止が簡単

## 注意点

- 初回ビルドには時間がかかります（Ubuntu + Rust のダウンロード）
- Docker Desktop のリソース設定を適切に行ってください
- コンテナ内での作業なので、ホストのファイルは `/workspace` にマウントされます

## 参考資料

- [Rust Zero GitHub](https://github.com/ytakano/rust_zero)
- [Docker Documentation](https://docs.docker.com/)
- [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) 