from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class JiraIssue(BaseModel):
    id: int
    url: str
    jira_id: str = Field(...,max_length=200)
    jira_key: str = Field(...,max_length=200)
    jira_creation: Optional[datetime] = None
    jira_change: Optional[datetime] = None
    jira_project: Optional[int] = None
    finding: Optional[int] = None
    engagement: Optional[int] = None
    finding_group: Optional[int] = None

