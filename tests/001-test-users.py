import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


BASE_URL = 'http://%s:%s/api/v1' % (HOST, PORT)


@t.ApiRequest()
def test_get_users(api):
    req = api.get_users()
    path = ENDPOINTS['users']['list']['name']
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS['users']['list']['method'])
    t.eq(api.response.status_int, 200)
    t.isin('items', req)
    t.isin('meta', req)
    t.eq(req['items'][0]['username'], 'fuzzy@example.com')
    t.eq(req['meta']['total'], 2)


@t.ApiRequest()
def test_get_user(api):
    userid = 5
    req = api.get_user(userid)
    path = ENDPOINTS['users']['get']['name'] % dict(userid=userid)
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS['users']['get']['method'])
    t.eq(api.response.status_int, 200)
    t.isin('username', req)
    t.isin('email', req)
    t.eq(req['username'], 'rowdyrough')
    t.eq(req['email'], 'rowdyrough@example.com')
    t.raises(BaruwaAPIError, api.get_user, 7)


@t.ApiRequest()
def test_create_user(api):
    data = {
        "username": "blossom",
        "firstname": "Blossom",
        "lastname": "Utonium",
        "password1": "ng5qhhbiwozcANc3",
        "password2": "ng5qhhbiwozcANc3",
        "email": "blossom@example.com",
        "timezone": "Africa/Johannesburg",
        "account_type": "3",
        "domains": "9",
        "active": "y",
        "send_report": "y",
        "spam_checks": "y",
        "low_score": "0.0",
        "high_score": "0.0"}
    req = api.create_user(data)
    path = ENDPOINTS['users']['new']['name']
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS['users']['new']['method'])
    t.eq(api.response.status_int, 201)
    t.isin('username', req)
    t.isin('email', req)
    t.eq(req['id'], 10)
    t.eq(req['username'], 'blossom')
    t.eq(req['email'], 'blossom@example.com')
    t.isnotin('password1', req)


@t.ApiRequest()
def test_update_user(api):
    data = {
        "username": "blossom",
        "firstname": "Blossom",
        "lastname": "Utonium",
        "password1": "ng5qhhbiwozcANc3",
        "password2": "ng5qhhbiwozcANc3",
        "email": "blossom@example.com",
        "timezone": "Africa/Johannesburg",
        "account_type": "3",
        "domains": "9",
        "active": "y",
        "send_report": "y",
        "spam_checks": "y",
        "low_score": "5.0",
        "high_score": "10.0"}
    req = api.update_user(data)
    path = ENDPOINTS['users']['update']['name']
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS['users']['update']['method'])
    t.eq(api.response.status_int, 201)
    t.eq(req['low_score'], '5.0')
    t.eq(req['high_score'], '10.0')
    t.isnotin('password1', req)


@t.ApiRequest()
def test_delete_user(api):
    userid = 10
    req = api.delete_user(userid)
    path = ENDPOINTS['users']['delete']['name'] % dict(userid=userid)
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS['users']['delete']['method'])
    t.eq(api.response.status_int, 204)
