from main import app
from ..resources.audio_diarization_resource import  *

app.add_route('/audiodiarize', AudioDiarizationResource())
