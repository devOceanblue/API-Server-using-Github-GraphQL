from typing import Union, List

from fastapi import APIRouter, Query

from services.repository_info_service import RepositoryInfoService

repository_router = APIRouter(prefix="/repository")

@repository_router.get(
    "", description="get info about repositories "
)
async def get_advertisements(
    request: Union[List[str], None] = Query(default=None)
):
    repository_info_service = RepositoryInfoService()

    result = await repository_info_service.get_repositories_info(request)
    return result