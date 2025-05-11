from pydantic import BaseModel, Field


class FindingMeta(BaseModel):
    name: str = Field(...,max_length=120)
    value: str = Field(...,max_length=300)

    model_config = {
        "populate_by_name": True,
        "extra": "ignore",
    }

