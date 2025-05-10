from pydantic import BaseModel

from .jira_issue import JiraIssue

class FindingGroup(BaseModel):
    id: int
    name: str
    test: int
    jira_issue: JiraIssue

