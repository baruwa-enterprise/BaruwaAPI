import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


API_PATH = '/api/v1'
BASE_URL = 'http://%s:%s' % (HOST, PORT)


@t.ApiRequest()
def test_list_deliveryservers(api):
    domainid = 9
    req = api.get_deliveryservers(domainid)
    path = ENDPOINTS['deliveryservers']['list']['name'] % dict(
        domainid=domainid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['deliveryservers']['list']['method'])
    t.eq(api.response.status_int, 200)
    t.isin('items', req)
    t.isin('meta', req)
    t.eq(req['items'][0]['address'], '192.168.1.150')
    t.eq(req['meta']['total'], 1)


@t.ApiRequest()
def test_get_deliveryserver(api):
    domainid = 9
    serverid = 4
    req = api.get_deliveryserver(domainid, serverid)
    path = ENDPOINTS['deliveryservers']['get']['name'] % dict(
        domainid=domainid, serverid=serverid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['deliveryservers']['get']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['address'], '192.168.1.151')
    t.raises(BaruwaAPIError, api.get_deliveryserver, 7, 1)


@t.ApiRequest()
def test_create_deliveryserver(api):
    domainid = 9
    data = {
        "address": "192.168.1.152",
        "protocol": "1",
        "port": "25",
        "enabled": "y"
    }
    req = api.create_deliveryserver(domainid, data)
    path = ENDPOINTS['deliveryservers']['new']['name'] % dict(
        domainid=domainid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['deliveryservers']['new']['method'])
    t.eq(api.response.status_int, 201)
    t.eq(req['address'], '192.168.1.152')


@t.ApiRequest()
def test_update_deliveryserver(api):
    domainid = 9
    serverid = 4
    data = {
        "address": "192.168.1.153",
        "protocol": "1",
        "port": "25",
        "enabled": "y"
    }
    req = api.update_deliveryserver(domainid, serverid, data)
    path = ENDPOINTS['deliveryservers']['update']['name'] % dict(
        domainid=domainid, serverid=serverid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['deliveryservers']['update']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['address'], '192.168.1.153')


@t.ApiRequest()
def test_delete_deliveryserver(api):
    domainid = 9
    serverid = 4
    data = {
        "address": "192.168.1.153",
    }
    req = api.delete_deliveryserver(domainid, serverid, data)
    path = ENDPOINTS['deliveryservers']['delete']['name'] % dict(
        domainid=domainid, serverid=serverid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['deliveryservers']['delete']['method'])
    t.eq(api.response.status_int, 204)
    t.eq(req['code'], 204)
