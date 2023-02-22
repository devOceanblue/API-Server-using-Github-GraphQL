import logging

from fastapi import FastAPI
from fastapi.logger import logger
from starlette.middleware.cors import CORSMiddleware

import config
from routes import main_router


def get_application():
    app = FastAPI()
    app.include_router(main_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    logger.setLevel(config.log_level)
    return app



app = get_application()

@app.on_event("startup")
async def on_start_up():
    logger.info("on_start_up")


@app.on_event("shutdown")
async def on_start_up():
    logger.info("on_shutdown")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
