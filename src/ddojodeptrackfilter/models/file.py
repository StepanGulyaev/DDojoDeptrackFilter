from pydantic import BaseModel

class File(BaseModel):
    id: int
    file: str
    title: str
