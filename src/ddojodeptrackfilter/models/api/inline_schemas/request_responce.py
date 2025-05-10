from datetime import date, datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class RequestResponse(BaseModel):
    req_resp: List[Dict[str, str]] = Field(default_factory=list)

    model_config = {
        "populate_by_name": True,
        "extra": "ignore",
    }

