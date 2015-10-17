import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS


BASE_URL = 'http://%s:%s/api/v1' % (HOST, PORT)


@t.ApiRequest()
def test_status(api):
    req = api.get_status()
    path = ENDPOINTS['status']['name']
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS['status']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['inbound'], 0)
