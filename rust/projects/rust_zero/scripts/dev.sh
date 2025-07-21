#!/bin/bash

# Rust Zero 開発環境管理スクリプト

set -e

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
    "restart")
        echo "🔄 Rust Zero 開発環境を再起動中..."
        docker-compose down
        docker-compose up -d
        echo "✅ 開発環境が再起動しました"
        ;;
    "logs")
        docker-compose logs -f
        ;;
    "shell")
        echo "🐚 コンテナ内でシェルを起動中..."
        docker-compose exec rust-dev bash
        ;;
    "build")
        echo "🔨 コンテナを再ビルド中..."
        docker-compose build --no-cache
        echo "✅ ビルドが完了しました"
        ;;
    "clean")
        echo "🧹 キャッシュをクリア中..."
        docker-compose down -v
        docker system prune -f
        echo "✅ クリーンアップが完了しました"
        ;;
    *)
        echo "使用方法: $0 {start|stop|restart|logs|shell|build|clean}"
        echo ""
        echo "コマンド:"
        echo "  start   - 開発環境を起動"
        echo "  stop    - 開発環境を停止"
        echo "  restart - 開発環境を再起動"
        echo "  logs    - ログを表示"
        echo "  shell   - コンテナ内でシェルを起動"
        echo "  build   - コンテナを再ビルド"
        echo "  clean   - キャッシュをクリア"
        exit 1
        ;;
esac 