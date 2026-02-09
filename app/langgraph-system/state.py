from pydantic import BaseModel



class IncidentCommanderState(BaseModel):
    alert_id: str
