import logging

from fastapi import APIRouter, Depends

from models.base_models.requests.repository import GetRepositoryRequest
from models.base_models.responses.repository import GetReposiotryResponse
from services.repository_info_service import RepositoryInfoService

repository_router = APIRouter(prefix="/repository")

@repository_router.get(
    "", description="get info about repositories "
)
async def get_advertisements(
    request: GetRepositoryRequest = Depends(), session=None
):
    repository_info_service = RepositoryInfoService()
    logging.warning(f'helllllllooooooo {request.names}')
    result = await repository_info_service.get_repositories_info([request.names])
    return result