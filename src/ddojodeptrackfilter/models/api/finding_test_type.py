from pydantic import BaseModel, Field

class FindingTestType(BaseModel):
    id: int
    name: str = Field(...,max_length=200) 

    model_config = {
        "populate_by_name": True,
        "extra": "ignore",
    }

