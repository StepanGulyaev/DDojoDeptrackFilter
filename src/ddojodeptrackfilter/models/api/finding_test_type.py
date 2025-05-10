from pydantic import BaseModel, Field

class FindingTestType(BaseModel):
    id: int
    name: str = Field(...,max_length=200) 

