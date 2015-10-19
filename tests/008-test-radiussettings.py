import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


API_PATH = '/api/v1'
BASE_URL = 'http://%s:%s' % (HOST, PORT)


@t.ApiRequest()
def test_get_radiussetting(api):
    domainid = 1
    serverid = 2
    settingsid = 3
    req = api.get_radiussettings(domainid, serverid, settingsid)
    path = ENDPOINTS['radiussettings']['get']['name'] % dict(
        domainid=domainid, serverid=serverid, settingsid=settingsid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['radiussettings']['get']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['timeout'], 30)
    t.raises(BaruwaAPIError, api.get_radiussettings, 7, 1, 4)


@t.ApiRequest()
def test_create_radiussetting(api):
    domainid = 1
    serverid = 2
    data = {
        "secret": "P4ssW0rd#",
        "timeout": "30"
    }
    req = api.create_radiussettings(domainid, serverid, data)
    path = ENDPOINTS['radiussettings']['new']['name'] % dict(
        domainid=domainid, serverid=serverid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['radiussettings']['new']['method'])
    t.eq(api.response.status_int, 201)
    t.eq(req['timeout'], '30')


@t.ApiRequest()
def test_update_radiussetting(api):
    domainid = 1
    serverid = 2
    settingsid = 3
    data = {
        "secret": "P4ssW0rd#2",
        "timeout": "35"
    }
    req = api.update_radiussettings(domainid, serverid, settingsid, data)
    path = ENDPOINTS['radiussettings']['update']['name'] % dict(
        domainid=domainid, serverid=serverid, settingsid=settingsid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['radiussettings']['update']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['timeout'], '35')


@t.ApiRequest()
def test_delete_radiussetting(api):
    domainid = 1
    serverid = 2
    settingsid = 3
    data = {
        "secret": "P4ssW0rd#2",
        "timeout": "30"
    }
    req = api.delete_radiussettings(domainid, serverid, settingsid, data)
    path = ENDPOINTS['radiussettings']['delete']['name'] % dict(
        domainid=domainid, serverid=serverid, settingsid=settingsid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['radiussettings']['delete']['method'])
    t.eq(api.response.status_int, 204)
    t.eq(req['code'], 204)
