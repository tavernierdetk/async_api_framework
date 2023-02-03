import falcon
import falcon.asgi
import requests
import os
from datetime import datetime as dt
import json

from Api.middleware.cors import *
# from pydub import AudioSegment
from pyannote.audio import Pipeline

diarization_pipeline = Pipeline.from_pretrained('pyannote/speaker-diarization', use_auth_token="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")

import re

app = falcon.asgi.App(
    middleware=[CorsMiddleware()]
)

from Api.routes import *

print('['+ dt.now().strftime('%Y-%m-%d %H:%M:%S') +']' + ' Routes loaded ! ✅')
print('['+ dt.now().strftime('%Y-%m-%d %H:%M:%S') +']' + ' This server is ready !')
