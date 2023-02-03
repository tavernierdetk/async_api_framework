# WSGI/API CORS Middleware and settings
ALLOWED_ORIGINS = ['*']
ALLOWED_HEADERS = ['Accept', 'Content-Type', 'X-CSRF-TOKEN', 'x-csrf-token', 'access-control-allow-origin']
ALLOWED_METHODS = ['GET', 'POST', 'UPDATE', 'DELETE', 'PATCH']


class CorsMiddleware(object):
    async def process_request(self, request, response):
        origin = request.get_header('Origin')

        if '*' in ALLOWED_ORIGINS:
            response.set_header('Access-Control-Allow-Origin', origin)

        if origin in ALLOWED_ORIGINS:
            response.set_header('Access-Control-Allow-Origin', origin)

    async def process_response(self, req, response, resource, req_succeeded):
        origin = req.get_header('Origin')
        if origin in ALLOWED_ORIGINS:
            response.set_header('Access-Control-Allow-Origin', origin)

            if(req_succeeded
                and req.method == 'OPTIONS'
                and req.get_header('Access-Control-Request-Method')
            ):
                allow = response.get_header('Allow')
                response.delete_header('Allow')

                allow_headers = req.get_header('Access-Control-Request-Headers', default='*')
                response.set_headers((
                    ('Access-Control-Allow-Methods', allow),
                    ('Access-Control-Allow-Headers', allow_headers),
                    ('Access-Control-Max-Age', '86400'),  # 24 hours
                ))