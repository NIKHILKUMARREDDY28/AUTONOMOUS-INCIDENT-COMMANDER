from operator import add
from typing import Annotated, Sequence

from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field


class IncidentCommanderState(BaseModel):
    messages: Annotated[Sequence[BaseMessage], add] = Field(default_factory=list)
