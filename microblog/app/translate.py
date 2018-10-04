import json, http.client, urllib.parse, uuid
import requests
from flask import current_app
from flask_babel import _

host = 'api.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'

params = "&to=de&to=it"

def translate(text):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    headers = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY'],
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    content = json.dumps([{'Text': text}], ensure_ascii=False).encode('utf-8')

    conn = http.client.HTTPSConnection(host)
    conn.request("POST", path + params, content, headers)
    response = conn.getresponse()

    result = response.read()
    return json.dumps(json.loads(result), indent=4, ensure_ascii=False)