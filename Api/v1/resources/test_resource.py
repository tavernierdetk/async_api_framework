import falcon
import falcon.asgi
import json
from ..schemas import json_schema
from datetime import datetime as dt
from ..schemas.test import *
import asyncio
import time

async def delay():
    time.sleep(5)
    print("Wait completed")

class GetTime(object):
    def __init__(self):
        super().__init__()

    async def on_get(self, req, res):
        print('incoming GET request')
        task = asyncio.create_task(delay())
        value = task
        res.status = falcon.HTTP_200
        res.json = {'time': dt.now().strftime("%m/%d/%Y, %H:%M:%S")}
        res.body = json.dumps(res.json)


    async def on_post(self, req, res):
        print('incoming POST request')
        res.status = falcon.HTTP_200
        res.json = {'time': dt.now().strftime("%m/%d/%Y, %H:%M:%S")}
        res.body = json.dumps(res.json)