from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

from .finding_prod_type import FindingProdType

class FindingProduct(BaseModel):
    id: int
    name: str = Field(...,max_length=255)
    prod_type: FindingProdType 
