from main import app
from ..resources.test_resource import *

app.add_route('/test/time', GetTime())