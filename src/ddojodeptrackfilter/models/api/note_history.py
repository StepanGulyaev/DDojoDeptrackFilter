from datetime import datetime
from pydantic import BaseModel

from .inline_schemas.note_user import NoteUser
from .note_type import NoteType

class NoteHistory(BaseModel):
    id: int
    current_editor: NoteUser
    note_type: NoteType
    data: str
    time: datetime

    model_config = {
        "populate_by_name": True,
        "extra": "ignore",
        "json_encoders": {
            datetime: lambda v: v.isoformat(),
        }
    }

