import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


BASE_URL = 'http://%s:%s/api/v1' % (HOST, PORT)


@t.ApiRequest()
def test_list_organizations(api):
    req = api.get_organizations()
    path = ENDPOINTS['organizations']['list']['name']
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['organizations']['list']['method'])
    t.eq(api.response.status_int, 200)
    t.isin('items', req)
    t.isin('meta', req)
    t.eq(req['items'][0]['name'], 'TDS')
    t.eq(req['meta']['total'], 3)


@t.ApiRequest()
def test_get_organization(api):
    orgid = 1
    req = api.get_organization(orgid)
    path = ENDPOINTS['organizations']['get']['name'] % dict(orgid=orgid)
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['organizations']['get']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['name'], 'My Org')
    t.raises(BaruwaAPIError, api.get_organization, 7)


@t.ApiRequest()
def test_create_organization(api):
    data = {
        "name": "My Org",
        "domains": "2",
        "domains": "4",
        "admins": "3"
    }
    req = api.create_organization(data)
    path = ENDPOINTS['organizations']['new']['name']
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['organizations']['new']['method'])
    t.eq(api.response.status_int, 201)
    t.eq(req['name'], 'My Org')


@t.ApiRequest()
def test_update_organization(api):
    orgid = 1
    data = {
        "name": "My Org2",
        "domains": "2",
        "domains": "4",
        "admins": "3"
    }
    req = api.update_organization(orgid, data)
    path = ENDPOINTS['organizations']['update']['name'] % dict(orgid=orgid)
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['organizations']['update']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['name'], 'My Org2')


@t.ApiRequest()
def test_delete_organization(api):
    orgid = 1
    req = api.delete_organization(orgid)
    path = ENDPOINTS['organizations']['delete']['name'] % dict(orgid=orgid)
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['organizations']['delete']['method'])
    t.eq(api.response.status_int, 204)
    t.eq(req['code'], 204)
