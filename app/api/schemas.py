from typing import List, Optional

from pydantic import BaseModel

class EventFilterParams(BaseModel):
    start_date: str
    end_date: str


class EventResponse(BaseModel):
    events: List[dict]


class ErrorModel(BaseModel):
    code: str
    msg: str
    
    def to_dict(self) -> dict:
        return [{"code": self.code, "msg": self.msg}]