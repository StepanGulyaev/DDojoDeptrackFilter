from pydantic import BaseModel, Field

class File(BaseModel):
    id: int
    file: str
    title: str = Field(..., max_length=100)
