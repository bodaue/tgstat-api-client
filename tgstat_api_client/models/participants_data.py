from pydantic import BaseModel


class ParticipantsData(BaseModel):
    period: str
    participants_count: int
