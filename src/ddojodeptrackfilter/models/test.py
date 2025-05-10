from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel, Field

from .finding_group import FindingGroup
from .note import Note
from .file import File

class TestModel(BaseModel):
    id: int
    tags: List[str] = Field(default_factory=list)
    test_type_name: str
    finding_groups: List[FindingGroup] = Field(default_factory=list)
    scan_type: str
    title: Optional[str]
    description: Optional[str]
    target_start: datetime
    target_end: datetime
    estimated_time: Optional[str]
    actual_time: Optional[str]
    percent_complete: int
    updated: datetime
    created: datetime
    version: str
    build_id: str
    commit_hash: str
    branch_tag: str
    engagement: int
    lead: Optional[int]
    test_type: int
    environment: int
    api_scan_configuration: Optional[Any]
    notes: List[Note] = Field(default_factory=list)
    files: List[File] = Field(default_factory=list)

    model_config = {
        "populate_by_name": True,
        "extra": "ignore",
        "json_encoders": {
            datetime: lambda v: v.isoformat()
        }
    }
