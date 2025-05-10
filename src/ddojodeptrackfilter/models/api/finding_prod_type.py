from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class FindingProdType(BaseModel):
    id: int
    name: str = Field(...,max_length=255)
