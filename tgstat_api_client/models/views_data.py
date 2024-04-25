from pydantic import BaseModel


class ViewsData(BaseModel):
    period: str
    views_count: int
