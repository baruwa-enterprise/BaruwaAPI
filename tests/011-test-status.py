import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS


API_PATH = '/api/v1'
BASE_URL = 'http://%s:%s' % (HOST, PORT)


@t.ApiRequest()
def test_status(api):
    req = api.get_status()
    path = ENDPOINTS['status']['name']
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(api.response.request.method, ENDPOINTS['status']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['inbound'], 0)
