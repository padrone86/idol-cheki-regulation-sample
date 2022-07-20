from typing import Type
from fastapi import FastAPI
from pydantic import BaseModel
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
import os
import uuid

TABLE_NAME = os.environ.get("TABLE_NAME")


class IdolGroupInput(BaseModel):
    name: str


class IdolGroup(Model):
    class Meta:
        host = f'http://{os.environ.get("DYNAMO_ENDPOINT", "localhost:8011")}'
        aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID", "idol-cheki")
        aws_secret_access_key = os.environ.get(
            "AWS_SECRET_ACCESS_KEY", "idol-cheki")
        region = os.environ.get("AWS_DEFAULT_REGION", "ap-northeast-1")
        table_name = os.environ.get("TABLE_NAME", "idol-groups")
    id: str = UnicodeAttribute(hash_key=True)
    name: str = UnicodeAttribute(null=True)


app = FastAPI()


@app.on_event("startup")
def startup_event():
    if not IdolGroup.exists():
        IdolGroup.create_table(read_capacity_units=1,
                               write_capacity_units=1, wait=True)


@app.post("/idol-groups/")
async def create_idol_group(idol_group_input: IdolGroupInput) -> IdolGroup:
    idol_group_id = str(uuid.uuid4())
    idol_group = IdolGroup(hash_key=idol_group_id, name=idol_group_input.name)
    idol_group.save()

    return idol_group


@app.get("/idol-groups/")
async def list_idol_group() -> dict[IdolGroup]:
    idol_groups = list()
    for i in IdolGroup.scan():
        idol_groups.append(i.attribute_values)
    return idol_groups


@app.get("/idol-groups/{idol_group_id}")
async def read_idol_group(idol_group_id: str) -> IdolGroup:
    idol_group = IdolGroup.get(hash_key=idol_group_id)
    return idol_group.attribute_values


@app.delete("/idol-groups/{idol_group_id}")
async def delete_idol_group(idol_group_id: str) -> None:
    target_idol_group = IdolGroup.get(idol_group_id)
    target_idol_group.delete()
