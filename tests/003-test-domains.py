import t

from _st import HOST, PORT
from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


BASE_URL = 'http://%s:%s/api/v1' % (HOST, PORT)


@t.ApiRequest()
def test_list_domains(api):
    req = api.get_domains()
    path = ENDPOINTS['domains']['list']['name']
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS['domains']['list']['method'])
    t.eq(api.response.status_int, 200)
    t.isin('items', req)
    t.isin('meta', req)
    t.eq(req['items'][0]['name'], 'example.com')
    t.eq(req['meta']['total'], 2)


@t.ApiRequest()
def test_get_domain(api):
    domainid = 1
    req = api.get_domain(domainid)
    path = ENDPOINTS['domains']['get']['name'] % dict(domainid=domainid)
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS['domains']['get']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['id'], 1)
    t.eq(req['name'], 'example.com')
    t.raises(BaruwaAPIError, api.get_domain, 7)


@t.ApiRequest()
def test_create_domain(api):
    data = {
        "name": "example.net",
        "site_url": "http://baruwa.example.net",
        "status": "y",
        "smtp_callout": "",
        "ldap_callout": "",
        "virus_checks": "y",
        "virus_checks_at_smtp": "y",
        "spam_checks": "y",
        "spam_actions": "3",
        "highspam_actions": "3",
        "virus_actions": "3",
        "low_score": "0.0",
        "high_score": "0.0",
        "message_size": "0",
        "delivery_mode": "1",
        "language": "en",
        "timezone": "Africa/Johannesburg",
        "report_every": "3",
        "organizations": "1"
    }
    req = api.create_domain(data)
    path = ENDPOINTS['domains']['new']['name']
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS['domains']['new']['method'])
    t.eq(api.response.status_int, 201)
    t.eq(req['name'], 'example.net')


@t.ApiRequest()
def test_update_domain(api):
    domainid = 3
    data = {
        "name": "example.net",
        "site_url": "http://baruwa.example.net",
        "status": "y",
        "smtp_callout": "",
        "ldap_callout": "",
        "virus_checks": "y",
        "virus_checks_at_smtp": "y",
        "spam_checks": "n",
        "spam_actions": "3",
        "highspam_actions": "3",
        "virus_actions": "3",
        "low_score": "0.0",
        "high_score": "0.0",
        "message_size": "0",
        "delivery_mode": "1",
        "language": "en",
        "timezone": "Africa/Johannesburg",
        "report_every": "3",
        "organizations": "1"
    }
    req = api.update_domain(domainid, data)
    path = ENDPOINTS['domains']['update']['name'] % dict(domainid=domainid)
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS['domains']['update']['method'])
    t.eq(api.response.status_int, 200)
    t.eq(req['spam_checks'], 'n')


@t.ApiRequest()
def test_delete_domain(api):
    domainid = 3
    req = api.delete_domain(domainid)
    path = ENDPOINTS['domains']['delete']['name'] % dict(domainid=domainid)
    t.eq(
        api.response.final_url,
        '%s%s' % (BASE_URL, path))
    t.eq(api.response.request.method, ENDPOINTS['domains']['delete']['method'])
    t.eq(api.response.status_int, 204)
    t.eq(req['code'], 204)
