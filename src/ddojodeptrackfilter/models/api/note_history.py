from datetime import datetime
from pydantic import BaseModel

from .note_user import NoteUser
from .inline_schemas.note_type import NoteType

class NoteHistory(BaseModel):
    id: int
    current_editor: NoteUser
    note_type: NoteType
    data: str
    time: datetime
