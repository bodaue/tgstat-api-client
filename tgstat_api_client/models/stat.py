from typing import Optional

from .base import Base


class Stat(Base):
    title: str
    username: Optional[str]
    participants_count: int


class StatChannel(Stat):
    avg_post_reach: Optional[int]
    adv_post_reach_12h: Optional[int]
    adv_post_reach_24h: Optional[int]
    adv_post_reach_48h: Optional[int]
    err_percent: Optional[float]
    err24_percent: Optional[float]
    er_percent: Optional[float]
    daily_reach: Optional[int]
    ci_index: Optional[float]
    mentions_count: Optional[int]
    forwards_count: Optional[int]
    mentioning_channels_count: Optional[int]
    posts_count: Optional[int]


class StatChat(Stat):
    dau: int
    wau: int
    mau: int
    online_count_day_time: int
    online_count_night_time: int
    messages_count_yesterday: int
    messages_count_last_week: int
    messages_count_last_month: int
    messages_count_total: int
