import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


BASE_URL = 'http://%s:%s/api/v1' % (HOST, PORT)


@t.ApiRequest()
def test_list_authservers(api):
    domainid = 9
    req = api.get_authservers(domainid)
    path = ENDPOINTS['authservers']['list']['name'] % dict(
        domainid=domainid)
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['authservers']['list']['method'])
    t.eq(api.response.status_int, 200)
    t.isin('items', req)
    t.isin('meta', req)
    t.eq(req['items'][0]['address'], '192.168.1.150')
    t.eq(req['meta']['total'], 1)


@t.ApiRequest()
def test_get_authserver(api):
    domainid = 9
    serverid = 4
    req = api.get_authserver(domainid, serverid)
    path = ENDPOINTS['authservers']['get']['name'] % dict(
        domainid=domainid, serverid=serverid)
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['authservers']['get']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['address'], '192.168.1.151')
    t.raises(BaruwaAPIError, api.get_deliveryserver, 7, 1)


@t.ApiRequest()
def test_create_authserver(api):
    domainid = 9
    data = {
        "address": "192.168.1.151",
        "protocol": "2",
        "port": "993",
        "enabled": "y",
        "split_address": "y",
        "user_map_template": "example_%(user)s"
    }
    req = api.create_authserver(domainid, data)
    path = ENDPOINTS['authservers']['new']['name'] % dict(
        domainid=domainid)
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['authservers']['new']['method'])
    t.eq(api.response.status_int, 201)
    t.eq(req['address'], '192.168.1.151')


@t.ApiRequest()
def test_update_authserver(api):
    domainid = 9
    serverid = 3
    data = {
        "address": "192.168.1.151",
        "protocol": "2",
        "port": "995",
        "enabled": "y",
        "split_address": "y",
        "user_map_template": "example_%(user)s"
    }
    req = api.update_authserver(domainid, serverid, data)
    path = ENDPOINTS['authservers']['update']['name'] % dict(
        domainid=domainid, serverid=serverid)
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['authservers']['update']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['port'], '995')


@t.ApiRequest()
def test_delete_authserver(api):
    domainid = 9
    serverid = 3
    data = {
        "address": "192.168.1.151",
        "protocol": "2",
        "port": "995",
        "enabled": "y",
        "split_address": "y",
        "user_map_template": "example_%(user)s"
    }
    req = api.delete_authserver(domainid, serverid, data)
    path = ENDPOINTS['authservers']['delete']['name'] % dict(
        domainid=domainid, serverid=serverid)
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['authservers']['delete']['method'])
    t.eq(api.response.status_int, 204)
