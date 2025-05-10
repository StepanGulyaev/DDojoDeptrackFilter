from pydantic import BaseModel, Field

class File(BaseModel):
    id: int
    file: str
    title: str = Field(..., max_length=100)

    model_config = {
        "populate_by_name": True,
        "extra": "ignore",
    }


