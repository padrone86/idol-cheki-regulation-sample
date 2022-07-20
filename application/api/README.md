# API

## 前提

- [Docker](https://docs.docker.com/get-docker/)
- [pipenv](https://pipenv-ja.readthedocs.io/ja/translate-ja/)
- [FastAPI](https://fastapi.tiangolo.com/ja/)

## FastAPI サーバの起動

pipenv スクリプトを用意してある。

```sh
# 通常起動
pipenv run server

# 開発用の起動 (reload オプションが ON)
pipenv run local_server
```

## ローカル開発用コンテナ環境

デモ用コンテナとは別に、ローカル開発用に以下のコンテナが起動するようになっている。

- DynamoDB
  - ※データはデモ環境と共有している
- dynamodb-admin

### 利用方法

基本的な動かし方は [デモ環境の手順](../README.md) と同じである。  
開発中の FastAPI から疎通できるように設定して利用する。
