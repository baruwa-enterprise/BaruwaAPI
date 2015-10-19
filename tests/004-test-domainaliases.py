import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


API_PATH = '/api/v1'
BASE_URL = 'http://%s:%s' % (HOST, PORT)


@t.ApiRequest()
def test_list_domainaliases(api):
    domainid = 9
    req = api.get_domainaliases(domainid)
    path = ENDPOINTS['domainaliases']['list']['name'] % dict(domainid=domainid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['domainaliases']['list']['method'])
    t.eq(api.response.status_int, 200)
    t.isin('items', req)
    t.isin('meta', req)
    t.eq(req['items'][0]['name'], 'example.net')
    t.eq(req['meta']['total'], 1)


@t.ApiRequest()
def test_get_domainalias(api):
    domainid = 9
    aliasid = 4
    req = api.get_domainalias(domainid, aliasid)
    path = ENDPOINTS['domainaliases']['get']['name'] % dict(
        domainid=domainid, aliasid=aliasid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['domainaliases']['get']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['name'], 'example.net')
    t.raises(BaruwaAPIError, api.get_domainalias, 7, 1)


@t.ApiRequest()
def test_create_domainalias(api):
    domainid = 9
    data = {
        "name": "example.net",
        "status": "y",
        "domain": "2",
    }
    req = api.create_domainalias(domainid, data)
    path = ENDPOINTS['domainaliases']['new']['name'] % dict(domainid=domainid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['domainaliases']['new']['method'])
    t.eq(api.response.status_int, 201)
    t.eq(req['name'], 'example.net')


@t.ApiRequest()
def test_update_domainalias(api):
    domainid = 9
    aliasid = 3
    data = {
        "name": "example.net",
        "status": "",
        "domain": "2",
    }
    req = api.update_domainalias(domainid, aliasid, data)
    path = ENDPOINTS['domainaliases']['update']['name'] % dict(
        domainid=domainid, aliasid=aliasid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['domainaliases']['update']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['name'], 'example.net')


@t.ApiRequest()
def test_delete_domainalias(api):
    domainid = 9
    aliasid = 3
    data = {
        "name": "example.net",
    }
    req = api.delete_domainalias(domainid, aliasid, data)
    path = ENDPOINTS['domainaliases']['delete']['name'] % dict(
        domainid=domainid, aliasid=aliasid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['domainaliases']['delete']['method'])
    t.eq(api.response.status_int, 204)
    t.eq(req['code'], 204)
