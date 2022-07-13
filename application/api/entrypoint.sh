#!/bin/sh

export AWS_ACCESS_KEY_ID=idol-cheki
export AWS_SECRET_ACCESS_KEY=idol-cheki
export AWS_DEFAULT_REGION=ap-northeast-1
export AWS_DEFAULT_OUTPUT=json

aws dynamodb list-tables --endpoint-url http://dynamodb-dev:8000 --no-cli-pager
