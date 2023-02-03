audio_diarization_schema_req = {
    "title": "audio_diarization_schema_req",
    "description": "A test endpoint for the ML/AI Api server",
    "type": "object",
    "properties": {
        "url": {
            "title": "url",
            "description": "url of media file to download",
            "type": "string"
        }
    },
    "required": ["url"]
}

audio_diarization_schema_resp = {
    "title": "audio_diarization_schema_resp",
    "description": "The ID of file to be downloaded",
    "produces": [
        "application/json",
    ],
    "type": "object",
    "properties": {
        "message": {
            "title": "message",
            "description": "A string",
            "type": "string"
        }
    },
    "required": ["message"]
}

audio_diarization_schema_req_get = {
    "title": "audio_diarization_schema_req_get",
    "description": "endpoint for fetching the end result of audio diarization using temporary file id",
    "type": "object",
    "properties": {
        "file_id": {
            "title": "file_id",
            "description": "the id of the file assigned to the endpoint",
            "type": "string"
        }
    },
    "required": ["file_id"]
}

audio_diarization_schema_resp_get = {
    "title": "audio_diarization_schema_resp_get",
    "description": "Listed speakers and timestamp of dialogue in the requested file",
    "produces": [
        "application/json",
    ],
    "type": "object",
    "properties": {
        "diarized_segment": {
            "title": "message",
            "description": "A string",
            "type": "string"
        }
    },
    "required": ["diarized_segment"]
}