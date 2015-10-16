import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


BASE_URL = 'http://%s:%s/api/v1' % (HOST, PORT)


@t.ApiRequest()
def test_status(api):
    pass
