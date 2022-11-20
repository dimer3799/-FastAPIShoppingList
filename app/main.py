# -*- coding: utf-8 -*-
from fastapi import FastAPI

from app.routers import ping

app = FastAPI()

app.include_router(ping.router)
