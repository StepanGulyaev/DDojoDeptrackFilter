from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel, Field

from .note import Note
from .finding_group import FindingGroup
from .file import File

class TestModel(BaseModel):
    id: int
    tags: List[str] = Field(default_factory=list)
    test_type_name: str
    finding_groups: List[FindingGroup]
    scan_type: Optional[str] = None
    title: Optional[str] = Field(None,max_length=255)
    description: Optional[str] = None
    target_start: datetime
    target_end: datetime
    estimated_time: Any
    actual_time: Any
    percent_complete: Optional[int] = None
    updated: datetime
    created: datetime
    version: Optional[str] = Field(None,max_length=100)
    build_id: Optional[str] = Field(None,max_length=150)    
    commit_hash: Optional[str] = Field(None,max_length=150)    
    branch_tag: Optional[str] = Field(None,max_length=150)
    engagement: int
    lead: Optional[int] = None
    test_type: int
    environment: Optional[int] = None
    api_scan_configuration: Optional[int] = None
    notes: List[Note]
    files: List[int]

    model_config = {
        "populate_by_name": True,
        "extra": "ignore",
        "json_encoders": {
            datetime: lambda v: v.isoformat()
        }
    }
