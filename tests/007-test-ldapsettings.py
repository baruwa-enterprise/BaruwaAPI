import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


API_PATH = '/api/v1'
BASE_URL = 'http://%s:%s' % (HOST, PORT)


@t.ApiRequest()
def test_get_ldapsetting(api):
    domainid = 1
    serverid = 2
    settingsid = 3
    req = api.get_ldapsettings(domainid, serverid, settingsid)
    path = ENDPOINTS['ldapsettings']['get']['name'] % dict(
        domainid=domainid, serverid=serverid, settingsid=settingsid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['ldapsettings']['get']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['basedn'], 'ou=Users,dc=example,dc=com')
    t.raises(BaruwaAPIError, api.get_ldapsettings, 7, 1, 4)


@t.ApiRequest()
def test_create_ldapsetting(api):
    domainid = 1
    serverid = 2
    data = {
        "basedn": "ou=Users,dc=example,dc=com",
        "nameattribute": "uid",
        "emailattribute": "mail",
        "binddn": "uid=readonly-admin,ou=Users,dc=example,dc=com",
        "bindpw": "P4ssW0rd",
        "usetls": "y",
        "search_scope": "subtree",
        "emailsearch_scope": "subtree"
    }
    req = api.create_ldapsettings(domainid, serverid, data)
    path = ENDPOINTS['ldapsettings']['new']['name'] % dict(
        domainid=domainid, serverid=serverid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['ldapsettings']['new']['method'])
    t.eq(api.response.status_int, 201)
    t.eq(req['basedn'], 'ou=Users,dc=example,dc=com')


@t.ApiRequest()
def test_update_ldapsetting(api):
    domainid = 1
    serverid = 2
    settingsid = 3
    data = {
        "basedn": "ou=Users,dc=example,dc=net",
        "nameattribute": "uid",
        "emailattribute": "mail",
        "binddn": "uid=readonly-admin,ou=Users,dc=example,dc=com",
        "bindpw": "P4ssW0rd",
        "usetls": "y",
        "search_scope": "subtree",
        "emailsearch_scope": "subtree"
    }
    req = api.update_ldapsettings(domainid, serverid, settingsid, data)
    path = ENDPOINTS['ldapsettings']['update']['name'] % dict(
        domainid=domainid, serverid=serverid, settingsid=settingsid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['ldapsettings']['update']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['basedn'], 'ou=Users,dc=example,dc=net')


@t.ApiRequest()
def test_delete_ldapsetting(api):
    domainid = 1
    serverid = 2
    settingsid = 3
    data = {
        "basedn": "ou=Users,dc=example,dc=net",
        "nameattribute": "uid",
        "emailattribute": "mail",
        "binddn": "uid=readonly-admin,ou=Users,dc=example,dc=com",
        "bindpw": "P4ssW0rd",
        "usetls": "y",
        "search_scope": "subtree",
        "emailsearch_scope": "subtree"
    }
    req = api.delete_ldapsettings(domainid, serverid, settingsid, data)
    path = ENDPOINTS['ldapsettings']['delete']['name'] % dict(
        domainid=domainid, serverid=serverid, settingsid=settingsid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(
        api.response.request.method,
        ENDPOINTS['ldapsettings']['delete']['method'])
    t.eq(api.response.status_int, 204)
    t.eq(req['code'], 204)
