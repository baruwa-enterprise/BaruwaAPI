import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


API_PATH = '/api/v1'
BASE_URL = 'http://%s:%s' % (HOST, PORT)


@t.ApiRequest()
def test_get_relay(api):
    relayid = 1
    req = api.get_relay(relayid)
    path = ENDPOINTS['relays']['get']['name'] % dict(relayid=relayid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(api.response.request.method, ENDPOINTS['relays']['get']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['address'], '192.168.1.20')
    t.raises(BaruwaAPIError, api.get_relay, 7)


@t.ApiRequest()
def test_create_relay(api):
    orgid = 1
    data = {
        "address": "192.168.1.20",
        "enabled": "y",
        "username": "outboundsmtp",
        "password1": "Str0ngP4ss##",
        "password2": "Str0ngP4ss##",
        "description": "Backup-outbound-smtp",
        "low_score": "10.0",
        "high_score": "15.0",
        "spam_actions": "2",
        "highspam_actions": "3"
    }
    req = api.create_relay(orgid, data)
    path = ENDPOINTS['relays']['new']['name'] % dict(orgid=orgid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(api.response.request.method, ENDPOINTS['relays']['new']['method'])
    t.eq(api.response.status_int, 201)
    t.eq(req['address'], '192.168.1.20')


@t.ApiRequest()
def test_update_relay(api):
    relayid = 1
    data = {
        "address": "192.168.1.21",
        "enabled": "y",
        "username": "outboundsmtp",
        "password1": "Str0ngP4ss##",
        "password2": "Str0ngP4ss##",
        "description": "Backup-outbound-smtp",
        "low_score": "10.0",
        "high_score": "15.0",
        "spam_actions": "2",
        "highspam_actions": "3"
    }
    req = api.update_relay(relayid, data)
    path = ENDPOINTS['relays']['update']['name'] % dict(relayid=relayid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(api.response.request.method, ENDPOINTS['relays']['update']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['address'], '192.168.1.21')


@t.ApiRequest()
def test_delete_relay(api):
    relayid = 1
    data = {
        "address": "192.168.1.21",
        "enabled": "y",
        "username": "outboundsmtp",
        "password1": "Str0ngP4ss##",
        "password2": "Str0ngP4ss##",
        "description": "Backup-outbound-smtp",
        "low_score": "10.0",
        "high_score": "15.0",
        "spam_actions": "2",
        "highspam_actions": "3"
    }
    req = api.delete_relay(relayid, data)
    path = ENDPOINTS['relays']['delete']['name'] % dict(relayid=relayid)
    t.eq(
        api.response.final_url,
        '%s%s%s' % (BASE_URL, API_PATH, path))
    t.eq(api.response.request.method, ENDPOINTS['relays']['delete']['method'])
    t.eq(api.response.status_int, 204)
    t.eq(req['code'], 204)
