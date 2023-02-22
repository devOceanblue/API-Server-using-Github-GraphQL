from typing import List

from fastapi import Query
from pydantic import BaseModel


class GetRepositoryRequest(BaseModel):
    names: str = Query(...)