from datetime import date, datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

from .inline_schemas.request_responce import RequestResponce 
from .inline_schemas.related_fields import RelatedFields

from .risk_acceptance import RiskAcceptance
from .finding_meta import FindingMeta
from .vulnerability_id import VulnerabilityID





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
    accepted_risks: List[RiskAcceptance]
    push_to_jira: Optional[bool] = None
    age: int
    sla_days_remaining: int
    finding_meta: List[FindingMeta]
    related_fields: RelatedFields
    jira_creation: datetime
    jira_change: datetime
    display_status: str
    finding_groups: List[FindingGroup] = Field(default_factory=list)
    vulnerability_ids: List[VulnerabilityID] = Field(default_factory=list)
    reporter: Optional[int] = None
    title: str = Field(...,max_length=511)
    date: Optional[date] = None
    sla_start_date: Optional[date] = None
    sla_expiration_date: Optional[date] = None
    cwe: Optional[int] = None
    epss_score: Optional[float] = Field(None,ge=0.0,le=1.0)
    epss_percentile: Optional[float] = Field(None,ge=0.0,le=1.0)
    cvssv3: Optional[str] = Field(None, pattern=r'^AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]')
    cvssv3_score: Optional[float] = Field(None,ge=0,le=10) 
    url: str
    severity: str = Field(...,max_length=200)
    description: str
    mitigation: Optional[str] = None
    impact: Optional[str] = None
    steps_to_reproduce: Optional[str] = None
    severity_justification: Optional[str] = None
    references: Optional[str] = None
    active: Optional[bool] = None
    verified: Optional[bool] = None
    false_p: Optional[bool] = None
    duplicate: Optional[bool] = None
    out_of_scope: Optional[bool] = None
    risk_accepted: Optional[bool] = None
    under_review: Optional[bool] = None
    last_status_update: datetime
    under_defect_review: Optional[bool] = None
    is_mitigated: Optional[bool] = None
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
