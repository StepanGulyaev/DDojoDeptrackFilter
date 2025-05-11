from datetime import date, datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class RiskAcceptance(BaseModel):
    id: int
    recommendation: str
    decision: str
    path: str
    name: str = Field(...,max_length=300)
    recommendation_details: Optional[str] = None
    decision_details: Optional[str] = None
    accepted_by: Optional[str] = Field(None,max_length=200)
    expiration_date: Optional[datetime]
    expiration_date_warned: Optional[datetime]
    expiration_date_handled: Optional[datetime]
    reactivate_expired: Optional[bool] = None
    restart_sla_expired: Optional[bool] = None
    created: datetime
    updated: datetime
    owner: int
    accepted_findings: List[int] = Field(default_factory=list)
    notes: List[int] = Field(default_factory=list)

    model_config = {
        "populate_by_name": True,
        "extra": "ignore",
        "json_encoders": {
            datetime: lambda v: v.isoformat(),
        }
    }

