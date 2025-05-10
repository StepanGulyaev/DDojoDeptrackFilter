from datetime import date, datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class RequestResponse(BaseModel):
    req_resp: List[Dict[str, str]] = Field(default_factory=list)

class AcceptedRisk(BaseModel):
    id: int
    recommendation: str
    decision: str
    path: str
    name: str
    recommendation_details: str
    decision_details: str
    accepted_by: str
    expiration_date: datetime
    expiration_date_warned: datetime
    expiration_date_handled: datetime
    reactivate_expired: bool
    restart_sla_expired: bool
    created: datetime
    updated: datetime
    owner: int
    accepted_findings: List[int] = Field(default_factory=list)
    notes: List[int] = Field(default_factory=list)

class FindingMetaEntry(BaseModel):
    name: str
    value: str


class TestTypeRef(BaseModel):
    id: int
    name: str


class ProductTypeRef(BaseModel):
    id: int
    name: str


class ProductRef(BaseModel):
    id: int
    name: str
    prod_type: ProductTypeRef


class EngagementRef(BaseModel):
    id: int
    name: str
    description: str
    product: ProductRef
    target_start: date
    target_end: date
    branch_tag: str
    engagement_type: str
    build_id: str
    commit_hash: str
    version: str
    created: datetime
    updated: datetime


class EnvironmentRef(BaseModel):
    id: int
    name: str


class TestRef(BaseModel):
    id: int
    title: str
    test_type: TestTypeRef
    engagement: EngagementRef
    environment: EnvironmentRef
    branch_tag: str
    build_id: str
    commit_hash: str
    version: str


class JiraIssueRef(BaseModel):
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


class JiraRef(BaseModel):
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


class RelatedFields(BaseModel):
    test: TestRef
    jira: JiraRef


class FindingGroup(BaseModel):
    id: int
    name: str
    test: int
    jira_issue: JiraIssueRef


class VulnerabilityID(BaseModel):
    vulnerability_id: str


class NoteAuthor(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str


class NoteHistory(BaseModel):
    id: int
    current_editor: NoteAuthor
    note_type: Any
    data: str
    time: datetime


class NoteTypeRef(BaseModel):
    id: int
    name: str
    description: str
    is_single: bool
    is_active: bool
    is_mandatory: bool


class Note(BaseModel):
    id: int
    author: NoteAuthor
    editor: Optional[NoteAuthor]
    history: List[NoteHistory] = Field(default_factory=list)
    note_type: NoteTypeRef
    entry: str
    date: datetime
    private: bool
    edited: bool
    edit_time: datetime


class FindingModel(BaseModel):
    id: int
    tags: List[str] = Field(default_factory=list)
    request_response: RequestResponse
    accepted_risks: List[AcceptedRisk] = Field(default_factory=list)
    push_to_jira: bool
    age: int
    sla_days_remaining: int
    finding_meta: List[FindingMetaEntry] = Field(default_factory=list)
    related_fields: RelatedFields
    jira_creation: datetime
    jira_change: datetime
    display_status: str
    finding_groups: List[FindingGroup] = Field(default_factory=list)
    vulnerability_ids: List[VulnerabilityID] = Field(default_factory=list)
    reporter: int
    title: str
    date: date
    sla_start_date: date
    sla_expiration_date: date
    cwe: int
    epss_score: float
    epss_percentile: float
    cvssv3: str
    cvssv3_score: float
    url: str
    severity: str
    description: str
    mitigation: str
    impact: str
    steps_to_reproduce: str
    severity_justification: str
    references: str
    active: bool
    verified: bool
    false_p: bool
    duplicate: bool
    out_of_scope: bool
    risk_accepted: bool
    under_review: bool
    last_status_update: datetime
    under_defect_review: bool
    is_mitigated: bool
    thread_id: int
    mitigated: datetime
    numerical_severity: str
    last_reviewed: datetime
    param: str
    payload: str
    hash_code: str
    line: int
    file_path: str
    component_name: str
    component_version: str
    static_finding: bool
    dynamic_finding: bool
    created: datetime
    scanner_confidence: int
    unique_id_from_tool: str
    vuln_id_from_tool: str
    sast_source_object: str
    sast_sink_object: str
    sast_source_line: int
    sast_source_file_path: str
    nb_occurences: int
    publish_date: date
    service: str
    planned_remediation_date: date
    planned_remediation_version: str
    effort_for_fixing: str
    test: int
    duplicate_finding: int
    review_requested_by: int
    defect_review_requested_by: int
    mitigated_by: int
    last_reviewed_by: int
    sonarqube_issue: int
    endpoints: List[int] = Field(default_factory=list)
    reviewers: List[int] = Field(default_factory=list)
    notes: List[Note] = Field(default_factory=list)
    files: List[int] = Field(default_factory=list)
    found_by: List[int] = Field(default_factory=list)

    model_config = {
        "populate_by_name": True,
        "extra": "ignore",
        "json_encoders": {
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
        }
    }
