from datetime import datetime
from pydantic import BaseModel

class JiraIssue(BaseModel):
    id: int
    url: str
    jira_id: str
    jira_key: str
    jira_creation: datetime
    jira_change: datetime
    jira_project: int
    finding: int
    engagement: int
    finding_group: int

