from typing import Optional

from pydantic import BaseModel

from .base import Base


class Media(BaseModel):
    file_url: Optional[str]
    caption: Optional[str] = ''


class Post(Base):
    date: int

    channel_id: int
    link: str
    forwarded_from: Optional[int]
    group_id: Optional[int]
    is_deleted: int
    deleted_at: Optional[int]
    text: str
    views: int
    media: Media
