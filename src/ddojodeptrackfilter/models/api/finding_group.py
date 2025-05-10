from pydantic import BaseModel, Field

from .jira_issue import JiraIssue

class FindingGroup(BaseModel):
    id: int
    name: str = Field(...,max_length=255)
    test: int
    jira_issue: JiraIssue

