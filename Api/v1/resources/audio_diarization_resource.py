import falcon
import falcon.asgi
import json
from ..schemas import json_schema
from datetime import datetime as dt
import time
import os


import ffmpeg
from ..schemas.audio_diarization import *
from main import diarization_pipeline
import asyncio

# TEST CLASS
# this is only to test the API

async def run_dowloader(url, file_id):
    ffmpeg.input(url).output(f"Files/AudioFiles/{file_id}.wav").run()
    AUDIO_FILE = {'uri': 'blabal', 'audio': f'Files/AudioFiles/{file_id}.wav'}
    dz = diarization_pipeline(AUDIO_FILE)
    with open("diarization.txt", "w") as text_file:
        text_file.write(str(dz))
    print(f'File ID {file_id} downloaded and diarized complete.')

class AudioDiarizationResource(object):
    def __init__(self):
        super().__init__()

    # @json_schema.validate(audio_diarization_schema_req_get, audio_diarization_schema_resp_get)
    async def on_get(self, req, res):
        print('incoming GET request')
        """Handles a test GET request."""

        res.status = falcon.HTTP_200  # This is the default status
        res.media = {"diarized_segment": "Come see on the server"}
        res.json = {"diarized_segment": "Come see on the server"}

    # @json_schema.validate(audio_diarization_schema_req, audio_diarization_schema_resp)
    async def on_post(self, req, res):
        print('incoming POST request')
        """Handles a test POST request."""
        file_id = f'{dt.now().minute}{dt.now().second}{dt.now().microsecond}'
        outfile_name = f"Files/AudioFiles/{file_id}.wav"
        url = req.params["url"]
        download = asyncio.create_task(run_dowloader(url, file_id))
        value = download

        res.status = falcon.HTTP_200  # This is the default status
        res.media = {"message": f"We're downloading the file, ID will be {outfile_name}"}
        res.json = {"message": f"We're downloading the file, ID will be {outfile_name}"}