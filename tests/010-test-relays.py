import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


BASE_URL = 'http://%s:%s/api/v1' % (HOST, PORT)


@t.ApiRequest()
def test_list_relays(api):
    pass


@t.ApiRequest()
def test_get_relay(api):
    pass


@t.ApiRequest()
def test_create_relay(api):
    pass


@t.ApiRequest()
def test_update_relay(api):
    pass


@t.ApiRequest()
def test_delete_relay(arg):
    pass
