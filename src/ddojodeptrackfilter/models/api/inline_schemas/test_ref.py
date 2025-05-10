from typing import Any, List, Optional
from pydantic import BaseModel, Field

from ..finding_test_type import FindingTestType
from ..finding_engagement import FindingEngagement
from ..finding_environment import FindingEnvironment

class TestRef(BaseModel):
    id: int
    title: Optional[str] = Field(None,max_length=255)
    test_type: Optional[FindingTestType] = None
    engagement: Optional[FindingEngagement] = None
    environment: Optional[FindingEnvironment] = None
    branch_tag: Optional[str] = Field(None,max_length=150)
    build_id: Optional[str] = Field(None,max_length=150)
    commit_hash: Optional[str] = Field(None,max_length=150)
    version: Optional[str] = Field(None,max_length=100)

