from pydantic import BaseModel, Field
from typing import Any,Optional, List
from datetime import datetime

class TestModel(BaseModel):
    id: int
    tags: List[str] = Field(default_factory=list)
    test_type_name: Optional[str]
    finding_groups: List[Any] = Field(default_factory=list)
    scan_type: Optional[str]
    title: Optional[str]
    description: Optional[str]
    target_start: Optional[datetime]
    target_end: Optional[datetime]
    estimated_time: Optional[Any]
    actual_time: Optional[Any]
    percent_complete: int
    updated: datetime
    created: datetime
    version: str
    build_id: str
    commit_hash: Optional[str]
    branch_tag: Optional[str]
    engagement: int
    lead: Optional[int]
    test_type: int
    environment: Optional[int]
    api_scan_configuration: Optional[Any]
    notes: List[Any] = Field(default_factory=list)
    files: List[Any] = Field(default_factory=list)
    
    model_config = {
        "populate_by_name": True,
        "extra": "ignore",
        "json_encoders": {
            datetime: lambda v: v.isoformat()
        }
    }
