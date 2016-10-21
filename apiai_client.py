import uuid
import requests
import logging
import json

log = logging.getLogger(__name__)


class APIAIClient(object):

    apiai_url = 'https://api.api.ai/v1'

    def __init__(self, token, lang="en"):
        self.token = token
        self.lang = lang
        self.session_id = unicode(uuid.uuid4())
        self._response = dict()

    @property
    def payload(self):
        return {
            "lang": self.lang,
            "sessionId": self.session_id
        }

    @property
    def headers(self):
        return {
            'Authorization': 'Bearer %s' % self.token,
            'content-type': 'application/json; charset=utf-8'
        }

    @property
    def speech(self):
        return self._response.get("speech", "")

    @property
    def action(self):
        return self._response.get("action")

    def run_query(self, query):
        payload = self.payload
        payload["query"] = query

        url = self.apiai_url + "/query"

        p = requests.post(url, headers=self.headers, json=payload)

        if p.status_code == 200:
            json_response = json.loads(p.content)
            # status_code = json_response.get(u'status', {}).get(u'code')

            self._response = json_response.get("result", dict())
        else:
            log.warning("Request Error: %s" % p.status_code)

