# アプリケーション

## ローカル開発用コンテナ環境

### 前提

- [Docker](https://docs.docker.com/get-docker/)
- [AWS CLI](https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/getting-started-install.html)

#### ローカル用 AWS CLI プロファイルの作成

[docker-compose.yml](./docker-compose.yml) の疎通情報と同じもので作成しておく。

```sh
$ aws configure --profile idol-cheki
AWS Access Key ID [None]: idol-cheki
AWS Secret Access Key [None]: idol-cheki
Default region name [None]: ap-northeast-1
Default output format [None]: json
```

#### 起動

```sh
$ docker compose up -d

# イメージの再ビルドをしたいとき
$ docker compose up --build
```

##### 疎通確認

`localhost:8011` が立ち上がるので、以下のコマンドで疎通確認できる。

```sh
$ aws dynamodb describe-limits --endpoint-url http://localhost:8011 --profile idol-cheki --no-cli-pager
{
    "AccountMaxReadCapacityUnits": 80000,
    "AccountMaxWriteCapacityUnits": 80000,
    "TableMaxReadCapacityUnits": 40000,
    "TableMaxWriteCapacityUnits": 40000
}
```

##### dynamodb-admin への接続

起動状態で以下 URL へアクセス。

- http://localhost:8013

#### 終了

```sh
$ docker compose down
```
