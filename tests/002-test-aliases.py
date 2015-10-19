import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


API_PATH = '/api/v1'
BASE_URL = 'http://%s:%s' % (HOST, PORT)


@t.ApiRequest()
def test_get_alias(api):
    addressid = 2
    req = api.get_aliases(addressid)
    path = ENDPOINTS['aliases']['get']['name'] % dict(addressid=addressid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(api.response.request.method, ENDPOINTS['aliases']['get']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['id'], addressid)
    t.eq(req['address'], 'info@example.com')
    t.raises(BaruwaAPIError, api.get_aliases, 7)


@t.ApiRequest()
def test_create_alias(api):
    userid = 2
    data = {
        "enabled": "y",
        "address": "info@example.com"
    }
    req = api.create_alias(userid, data)
    path = ENDPOINTS['aliases']['new']['name'] % dict(userid=userid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(api.response.request.method, ENDPOINTS['aliases']['new']['method'])
    t.eq(api.response.status_int, 201)
    t.eq(req['id'], 3)
    t.eq(req['enabled'], 'y')
    t.eq(req['address'], 'info@example.com')


@t.ApiRequest()
def test_update_alias(api):
    addressid = 3
    data = {
        "address": "info@example.com"
    }
    req = api.update_alias(addressid, data)
    path = ENDPOINTS['aliases']['update']['name'] % dict(addressid=addressid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(api.response.request.method, ENDPOINTS['aliases']['update']['method'])
    t.eq(api.response.status_int, 200)
    t.isnotin('enabled', req)
    t.eq(req['address'], 'info@example.com')


@t.ApiRequest()
def test_delete_alias(api):
    addressid = 3
    data = {
        "address": "info@example.com"
    }
    req = api.delete_alias(addressid, data)
    path = ENDPOINTS['aliases']['delete']['name'] % dict(addressid=addressid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(api.response.request.method, ENDPOINTS['aliases']['delete']['method'])
    t.eq(api.response.status_int, 204)
    t.eq(req['code'], 204)
