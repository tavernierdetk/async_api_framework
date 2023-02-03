test_schema_req = {
    "title": "test_schema_req",
    "description": "A test endpoint for the ML/AI Api server",
    "type": "object",
    "properties": {
        "query_body": { 
            "title": "query_body",
            "description": "A query string like : francois legault",
            "type": "string"
        }
    },
    "required": ["query_body"]
}

test_schema_resp = {
    "title": "test_schema_resp",
    "description": "A test response",
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

time_schema_req = {
    "title": "time_schema",
    "description": "A test endpoint that returns the time"

}