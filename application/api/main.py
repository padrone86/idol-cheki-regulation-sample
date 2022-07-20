from fastapi import FastAPI
from pydantic import BaseModel
import dataclasses
import uuid


class IdolGroupInput(BaseModel):
    name: str


@dataclasses.dataclass
class IdolGroup:
    id: str
    name: str


data = dict()

app = FastAPI()


@app.post("/idol-groups/")
async def create_idol_group(idol_group_input: IdolGroupInput) -> IdolGroup:
    idol_group_id = str(uuid.uuid4())
    idol_group = IdolGroup(idol_group_id, idol_group_input.name)
    global data
    data[idol_group_id] = idol_group
    print(idol_group_id)
    return idol_group


@app.get("/idol-groups/")
async def read_idol_groups() -> dict[IdolGroup]:
    return data


@app.get("/idol-groups/{idol_group_id}")
async def read_idol_group(idol_group_id: str) -> IdolGroup:
    return data[idol_group_id]


@app.delete("/idol-groups/{idol_group_id}")
async def delete_idol_group(idol_group_id: str) -> None:
    del data[idol_group_id]
