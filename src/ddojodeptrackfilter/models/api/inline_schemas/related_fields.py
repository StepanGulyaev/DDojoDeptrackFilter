from pydantic import BaseModel, Field

from ..jira_issue import JiraIssue
from .test_ref import TestRef

class RelatedFields(BaseModel):
    test: TestRef
    jira: JiraIssue

