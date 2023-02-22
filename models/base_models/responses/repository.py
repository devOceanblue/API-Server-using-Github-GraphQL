from typing import List

from pydantic import BaseModel


class RepositoryInfo(BaseModel):
    name: str
    description: str
    open_issues: str
    five_most_recent_issue_titles: str

class GetReposiotryResponse(BaseModel):
    result: List[RepositoryInfo]