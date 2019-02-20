import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


API_PATH = '/api/v1'
BASE_URL = 'http://%s:%s' % (HOST, PORT)


@t.ApiRequest()
def test_list_fallbackservers(api):
    orgid = 1
    req = api.get_fallbackservers(orgid)
    path = ENDPOINTS['fallbackservers']['list']['name'] % dict(orgid=orgid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['fallbackservers']['list']['method'])
    t.eq(api.response.status_int, 200)
    t.isin('items', req)
    t.isin('meta', req)
    t.eq(req['items'][0]['address'], '192.168.1.150')
    t.eq(req['meta']['total'], 1)


@t.ApiRequest()
def test_list_fallbackservers_paged(api):
    orgid = 1
    page = 1
    req = api.get_fallbackservers(orgid, page=page)
    path = ENDPOINTS['fallbackservers']['list']['name'] % dict(orgid=orgid)
    t.eq(
        api.response.final_url,
        '%s%s%s?page=%d' % (BASE_URL, API_PATH, path, page))
    t.eq(
        api.response.request.method,
        ENDPOINTS['fallbackservers']['list']['method'])
    t.eq(api.response.status_int, 200)
    t.isin('items', req)
    t.isin('meta', req)
    t.eq(req['items'][0]['address'], '192.168.1.150')
    t.eq(req['meta']['total'], 1)


@t.ApiRequest()
def test_get_fallbackserver(api):
    serverid = 9
    req = api.get_fallbackserver(serverid)
    path = ENDPOINTS['fallbackservers']['get']['name'] % \
        dict(serverid=serverid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['fallbackservers']['get']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['address'], '192.168.1.150')
    t.raises(BaruwaAPIError, api.get_fallbackserver, 7)


@t.ApiRequest()
def test_create_fallbackserver(api):
    orgid = 1
    data = {
        "address": "192.168.1.152",
        "protocol": "1",
        "port": "25",
        "enabled": "y"
    }
    req = api.create_fallbackserver(orgid, data)
    path = ENDPOINTS['fallbackservers']['new']['name'] % dict(orgid=orgid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['fallbackservers']['new']['method'])
    t.eq(api.response.status_int, 201)
    t.eq(req['address'], '192.168.1.152')


@t.ApiRequest()
def test_update_fallbackserver(api):
    serverid = 9
    data = {
        "address": "192.168.1.153",
        "protocol": "1",
        "port": "25",
        "enabled": "y"
    }
    req = api.update_fallbackserver(serverid, data)
    path = ENDPOINTS['fallbackservers']['update']['name'] % \
        dict(serverid=serverid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['fallbackservers']['update']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['address'], '192.168.1.153')


@t.ApiRequest()
def test_delete_fallbackserver(api):
    serverid = 9
    data = {
        "address": "192.168.1.153",
    }
    req = api.delete_fallbackserver(serverid, data)
    path = ENDPOINTS['fallbackservers']['delete']['name'] % \
        dict(serverid=serverid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['fallbackservers']['delete']['method'])
    t.eq(api.response.status_int, 204)
    t.eq(req['code'], 204)
