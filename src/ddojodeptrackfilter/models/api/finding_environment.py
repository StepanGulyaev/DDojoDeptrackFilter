from typing import Any, List, Optional
from pydantic import BaseModel, Field

class FindingEnvironment(BaseModel):
    id: int
    name: str = Field(...,max_length=200)

