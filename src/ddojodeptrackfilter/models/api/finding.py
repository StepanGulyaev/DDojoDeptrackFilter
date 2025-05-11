from datetime import date, datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

from .inline_schemas.request_responce import RequestResponse 
from .inline_schemas.related_fields import RelatedFields

from .risk_acceptance import RiskAcceptance
from .finding_meta import FindingMeta
from .finding_group import FindingGroup
from .vulnerability_id import VulnerabilityID
from .note import Note


class Finding(BaseModel):
    id: int
    tags: List[str] = Field(default_factory=list)
    request_response: RequestResponse
    accepted_risks: List[RiskAcceptance] = Field(default_factory=list)
    push_to_jira: Optional[bool] = None
    age: int
    sla_days_remaining: Optional[int] = None
    finding_meta: List[FindingMeta] = Field(default_factory=list)
    related_fields: Optional[RelatedFields] = None
    jira_creation: Optional[datetime] = None
    jira_change: Optional[datetime] = None
    display_status: str
    finding_groups: List[FindingGroup] = Field(default_factory=list)
    vulnerability_ids: List[VulnerabilityID] = Field(default_factory=list)
    reporter: Optional[int] = None
    title: str = Field(...,max_length=511)
    date: date
    sla_start_date: Optional[date] = None
    sla_expiration_date: Optional[date] = None
    cwe: Optional[int] = None
    epss_score: Optional[float] = Field(None,ge=0.0,le=1.0)
    epss_percentile: Optional[float] = Field(None,ge=0.0,le=1.0)
    cvssv3: Optional[str] = Field(None, pattern=r'^AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]')
    cvssv3_score: Optional[float] = Field(None,ge=0,le=10) 
    url: Optional[str] = None
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
    mitigated: Optional[datetime] = None
    numerical_severity: str = Field(...,max_length=4)
    last_reviewed: datetime
    param: Optional[str] = None
    payload: Optional[str] = None
    hash_code: str
    line: Optional[int]
    file_path: Optional[str] = Field(None,max_length=4000)
    component_name: Optional[str] = Field(None,max_length=500)
    component_version: Optional[str] = Field(None,max_length=100)
    static_finding: Optional[bool] = None
    dynamic_finding: Optional[bool] = None
    created: datetime
    scanner_confidence: Optional[int] = None
    unique_id_from_tool: Optional[str] = Field(None,max_length=500)
    vuln_id_from_tool: Optional[str] = Field(None,max_length=500)
    sast_source_object: Optional[str] = Field(None,max_length=500)
    sast_sink_object: Optional[str] = Field(None,max_length=500)
    sast_source_line: Optional[int] = None
    sast_source_file_path: Optional[str] = Field(None,max_length=4000)
    nb_occurences: Optional[int] = None
    publish_date: Optional[date]
    service: Optional[str] = Field(None,max_length=200)
    planned_remediation_date: Optional[date] = None
    planned_remediation_version: Optional[str] = Field(None,max_length=99)
    effort_for_fixing: Optional[str] = Field(None,max_length=99)
    test: int
    duplicate_finding: Optional[int] = None
    review_requested_by: Optional[int] = None
    defect_review_requested_by: Optional[int] = None
    mitigated_by: Optional[int] = None
    last_reviewed_by: int
    sonarqube_issue: Optional[int] = None
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
