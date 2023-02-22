from fastapi import APIRouter

from routes.repository_info import repository_router

main_router = APIRouter(prefix="")

blueprints = [repository_router]


for router in blueprints:
    main_router.include_router(router)