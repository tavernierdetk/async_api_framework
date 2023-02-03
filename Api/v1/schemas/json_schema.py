from __future__ import absolute_import
from functools import wraps
import falcon

try:
    import jsonschema
except ImportError:
    pass


def validate(req_schema=None, resp_schema=None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, req, resp, *args, **kwargs):
            if req.method == "GET":
                incoming_data = req.params
            elif req.method in ["POST", "UPDATE", "DELETE", "PUT"]:
                incoming_data = req.media
            else:
                raise falcon.HTTPMethodNotAllowed('Unsupported method')
            
            if req_schema is not None:
                try:
                    jsonschema.validate(
                        incoming_data, req_schema,
                        format_checker=jsonschema.FormatChecker()
                    )
                except jsonschema.ValidationError as e:
                    raise falcon.HTTPBadRequest(
                        'Request data failed validation',
                        description=e.message
                    )

            result = func(self, req, resp, *args, **kwargs)

            if resp_schema is not None:
                try:
                    jsonschema.validate(
                        resp.media, resp_schema,
                        format_checker=jsonschema.FormatChecker()
                    )
                except jsonschema.ValidationError:
                    raise falcon.HTTPInternalServerError(
                        'Response data failed validation'
                        # Do not return 'e.message' in the response to
                        # prevent info about possible internal response
                        # formatting bugs from leaking out to users.
                    )

            return result
        return wrapper
    return decorator
