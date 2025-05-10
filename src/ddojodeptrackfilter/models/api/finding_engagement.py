from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel, Field

from .finding_product import FindingProduct

class FindingEngagement(BaseModel):
    id: int
    name: Optional[str] = Field(None,max_length=300)
    description: Optional[str] = Field(None,max_length=2000)
    product: FindingProduct
    target_start: date
    target_end: date
    branch_tag: Optional[str] = Field(None,max_length=150)
    engagement_type: Optional[str] = Field(None,pattern=r'^(Interactive|CI/CD)$')
    build_id: Optional[str] = Field(None,max_length=150)
    commit_hash: Optional[str] = Field(None,max_length=150)
    version: Optional[str] = Field(None,max_length=100)
    created: datetime
    updated: datetime
