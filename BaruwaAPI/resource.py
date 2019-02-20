# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# BaruwaAPI Python bindings for Baruwa REST API
# Copyright (C) 2015-2019 Andrew Colin Kissa <andrew@topdog.za.net>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""
BaruwaAPI resources
"""

import json

from restkit import Resource

from BaruwaAPI.endpoints import ENDPOINTS
from BaruwaAPI.exceptions import BaruwaAPIError


# pylint: disable=too-many-public-methods
class BaruwaAPIClient(Resource):
    """BaruwaAPIClient class"""

    def __init__(self, api_token, api_url='https://localhost', **kwargs):
        """Init"""
        super(BaruwaAPIClient, self).__init__(api_url, ssl_version=3,
                                              **kwargs)
        self.api_token = api_token
        self.response = None

    def _request_headers(self):
        """Return the required API headers"""
        return {'Authorization': "Bearer %s" % self.api_token,
                'User-Agent': 'BaruwaAPI-Python',
                'Content-Type': 'application/json'}

    def _request(self, *args, **kwargs):
        """Make the request"""
        try:
            self.response = self.request(
                *args, headers=self._request_headers(), **kwargs)
        except BaseException, err:
            code = 520
            if hasattr(err, 'status_int'):
                code = err.status_int  # pylint: disable=no-member
            if hasattr(err, 'message'):
                message = err.message
            raise BaruwaAPIError(code, message)
        if self.response.status_int in [200, 201, 204]:
            body = self.response.body_string()
            if not body:
                body = '{"code":%d,"message":"Completed successfully"}' % \
                    self.response.status_int
        else:
            raise BaruwaAPIError(
                code=self.response.status_int,
                message=self.response.body_string())
        return json.loads(body)

    def api_call(self, opts, args=None, body=None, **kwargs):
        """Setup the request"""
        if args:
            path = opts['name'] % args
        else:
            path = opts['name']
        path = '/api/v1%s' % path
        return self._request(
            opts['method'], path=path, payload=body, **kwargs)

    def get_users(self, page=None):
        """Get users"""
        opts = {}
        if page:
            opts['page'] = page
        return self.api_call(ENDPOINTS['users']['list'], **opts)

    def get_user(self, userid):
        """Get user"""
        return self.api_call(ENDPOINTS['users']['get'], dict(userid=userid))

    def create_user(self, data):
        """Create user"""
        return self.api_call(ENDPOINTS['users']['new'], body=data)

    def update_user(self, data):
        """Update user"""
        return self.api_call(ENDPOINTS['users']['update'], body=data)

    def delete_user(self, userid):
        """Delete user"""
        return self.api_call(ENDPOINTS['users']['delete'], dict(userid=userid))

    def set_user_passwd(self, userid, data):
        """Set user password"""
        return self.api_call(
            ENDPOINTS['users']['password'],
            dict(userid=userid),
            body=data)

    def get_aliases(self, addressid):
        """Get alias addresses"""
        return self.api_call(
            ENDPOINTS['aliases']['get'],
            dict(addressid=addressid))

    def create_alias(self, userid, data):
        """Create alias address"""
        return self.api_call(
            ENDPOINTS['aliases']['new'],
            dict(userid=userid),
            body=data)

    def update_alias(self, addressid, data):
        """Update alias address"""
        return self.api_call(
            ENDPOINTS['aliases']['update'],
            dict(addressid=addressid),
            body=data)

    def delete_alias(self, addressid, data):
        """Delete alias address"""
        return self.api_call(
            ENDPOINTS['aliases']['delete'],
            dict(addressid=addressid),
            body=data)

    def get_domains(self, page=None):
        """Get domains"""
        opts = {}
        if page:
            opts['page'] = page
        return self.api_call(ENDPOINTS['domains']['list'], **opts)

    def get_domain(self, domainid):
        """Get a domain"""
        return self.api_call(
            ENDPOINTS['domains']['get'],
            dict(domainid=domainid))

    def get_domain_by_name(self, domainname):
        """Get a domain by name"""
        return self.api_call(
            ENDPOINTS['domains']['get_by_name'],
            dict(domainname=domainname))

    def create_domain(self, data):
        """Create a domain"""
        return self.api_call(ENDPOINTS['domains']['new'], body=data)

    def update_domain(self, domainid, data):
        """Update a domain"""
        return self.api_call(
            ENDPOINTS['domains']['update'],
            dict(domainid=domainid),
            body=data)

    def delete_domain(self, domainid):
        """Delete a domain"""
        return self.api_call(
            ENDPOINTS['domains']['delete'],
            dict(domainid=domainid))

    def get_domainaliases(self, domainid, page=None):
        """Get Domain aliases"""
        opts = {}
        if page:
            opts['page'] = page
        return self.api_call(
            ENDPOINTS['domainaliases']['list'],
            dict(domainid=domainid), **opts)

    def get_domainalias(self, domainid, aliasid):
        """Get a Domain alias"""
        return self.api_call(
            ENDPOINTS['domainaliases']['get'],
            dict(domainid=domainid, aliasid=aliasid))

    def create_domainalias(self, domainid, data):
        """Create a domain alias"""
        return self.api_call(
            ENDPOINTS['domainaliases']['new'],
            dict(domainid=domainid),
            body=data)

    def update_domainalias(self, domainid, aliasid, data):
        """Update a domain alias"""
        return self.api_call(
            ENDPOINTS['domainaliases']['update'],
            dict(domainid=domainid, aliasid=aliasid),
            body=data)

    def delete_domainalias(self, domainid, aliasid, data):
        """Delete a domain alias"""
        return self.api_call(
            ENDPOINTS['domainaliases']['delete'],
            dict(domainid=domainid, aliasid=aliasid),
            body=data)

    def get_deliveryservers(self, domainid, page=None):
        """Get a domains delivery servers"""
        opts = {}
        if page:
            opts['page'] = page
        return self.api_call(
            ENDPOINTS['deliveryservers']['list'],
            dict(domainid=domainid), **opts)

    def get_deliveryserver(self, domainid, serverid):
        """Get a delivery server"""
        return self.api_call(
            ENDPOINTS['deliveryservers']['get'],
            dict(domainid=domainid, serverid=serverid))

    def create_deliveryserver(self, domainid, data):
        """Create a delivery server"""
        return self.api_call(
            ENDPOINTS['deliveryservers']['new'],
            dict(domainid=domainid),
            body=data)

    def update_deliveryserver(self, domainid, serverid, data):
        """Update a delivery server"""
        return self.api_call(
            ENDPOINTS['deliveryservers']['update'],
            dict(domainid=domainid, serverid=serverid),
            body=data)

    def delete_deliveryserver(self, domainid, serverid, data):
        """Delete a delivery server"""
        return self.api_call(
            ENDPOINTS['deliveryservers']['delete'],
            dict(domainid=domainid, serverid=serverid),
            body=data)

    def get_user_deliveryserver(self, domainid, serverid):
        """Get a user delivery server"""
        return self.api_call(
            ENDPOINTS['userdeliveryservers']['get'],
            dict(domainid=domainid, serverid=serverid))

    def create_user_deliveryserver(self, domainid, data):
        """Create a user delivery server"""
        return self.api_call(
            ENDPOINTS['userdeliveryservers']['new'],
            dict(domainid=domainid),
            body=data)

    def update_user_deliveryserver(self, domainid, serverid, data):
        """Update a user delivery server"""
        return self.api_call(
            ENDPOINTS['userdeliveryservers']['update'],
            dict(domainid=domainid, serverid=serverid),
            body=data)

    def delete_user_deliveryserver(self, domainid, serverid, data):
        """Delete a user delivery server"""
        return self.api_call(
            ENDPOINTS['userdeliveryservers']['delete'],
            dict(domainid=domainid, serverid=serverid),
            body=data)

    def get_domain_smarthost(self, domainid, serverid):
        """Get a domain smarthost"""
        return self.api_call(
            ENDPOINTS['domainsmarthosts']['get'],
            dict(domainid=domainid, serverid=serverid))

    def create_domain_smarthost(self, domainid, data):
        """Create a domain smarthost"""
        return self.api_call(
            ENDPOINTS['domainsmarthosts']['new'],
            dict(domainid=domainid),
            body=data)

    def update_domain_smarthost(self, domainid, serverid, data):
        """Update a domain smarthost"""
        return self.api_call(
            ENDPOINTS['domainsmarthosts']['update'],
            dict(domainid=domainid, serverid=serverid),
            body=data)

    def delete_domain_smarthost(self, domainid, serverid, data):
        """Delete a domain smarthost"""
        return self.api_call(
            ENDPOINTS['domainsmarthosts']['delete'],
            dict(domainid=domainid, serverid=serverid),
            body=data)

    def get_authservers(self, domainid, page=None):
        """Get Authentication servers"""
        opts = {}
        if page:
            opts['page'] = page
        return self.api_call(
            ENDPOINTS['authservers']['list'],
            dict(domainid=domainid), **opts)

    def get_authserver(self, domainid, serverid):
        """Get an Authentication server"""
        return self.api_call(
            ENDPOINTS['authservers']['get'],
            dict(domainid=domainid, serverid=serverid))

    def create_authserver(self, domainid, data):
        """Create an Authentication server"""
        return self.api_call(
            ENDPOINTS['authservers']['new'],
            dict(domainid=domainid),
            body=data)

    def update_authserver(self, domainid, serverid, data):
        """Update an Authentication server"""
        return self.api_call(
            ENDPOINTS['authservers']['update'],
            dict(domainid=domainid, serverid=serverid),
            body=data)

    def delete_authserver(self, domainid, serverid, data):
        """Delete an Authentication server"""
        return self.api_call(
            ENDPOINTS['authservers']['delete'],
            dict(domainid=domainid, serverid=serverid),
            body=data)

    def get_ldapsettings(self, domainid, serverid, settingsid):
        """Get LDAP settings"""
        return self.api_call(
            ENDPOINTS['ldapsettings']['get'],
            dict(domainid=domainid, serverid=serverid, settingsid=settingsid))

    def create_ldapsettings(self, domainid, serverid, data):
        """Create LDAP settings"""
        return self.api_call(
            ENDPOINTS['ldapsettings']['new'],
            dict(domainid=domainid, serverid=serverid),
            body=data)

    def update_ldapsettings(self, domainid, serverid, settingsid, data):
        """Update LDAP settings"""
        return self.api_call(
            ENDPOINTS['ldapsettings']['update'],
            dict(domainid=domainid, serverid=serverid, settingsid=settingsid),
            body=data)

    def delete_ldapsettings(self, domainid, serverid, settingsid, data):
        """Delete LDAP settings"""
        return self.api_call(
            ENDPOINTS['ldapsettings']['delete'],
            dict(domainid=domainid, serverid=serverid, settingsid=settingsid),
            body=data)

    def get_radiussettings(self, domainid, serverid, settingsid):
        """Get RADIUS settings"""
        return self.api_call(
            ENDPOINTS['radiussettings']['get'],
            dict(domainid=domainid, serverid=serverid, settingsid=settingsid))

    def create_radiussettings(self, domainid, serverid, data):
        """Create RADIUS settings"""
        return self.api_call(
            ENDPOINTS['radiussettings']['new'],
            dict(domainid=domainid, serverid=serverid),
            body=data)

    def update_radiussettings(self, domainid, serverid, settingsid, data):
        """Update RADIUS settings"""
        return self.api_call(
            ENDPOINTS['radiussettings']['update'],
            dict(domainid=domainid, serverid=serverid, settingsid=settingsid),
            body=data)

    def delete_radiussettings(self, domainid, serverid, settingsid, data):
        """Delete RADIUS settings"""
        return self.api_call(
            ENDPOINTS['radiussettings']['delete'],
            dict(domainid=domainid, serverid=serverid, settingsid=settingsid),
            body=data)

    def get_organizations(self, page=None):
        """Get organizations"""
        opts = {}
        if page:
            opts['page'] = page
        return self.api_call(ENDPOINTS['organizations']['list'], **opts)

    def get_organization(self, orgid):
        """Get an organization"""
        return self.api_call(
            ENDPOINTS['organizations']['get'],
            dict(orgid=orgid))

    def create_organization(self, data):
        """Create an organization"""
        return self.api_call(ENDPOINTS['organizations']['new'], body=data)

    def update_organization(self, orgid, data):
        """Update an organization"""
        return self.api_call(
            ENDPOINTS['organizations']['update'],
            dict(orgid=orgid),
            body=data)

    def delete_organization(self, orgid):
        """Delete an organization"""
        return self.api_call(
            ENDPOINTS['organizations']['delete'],
            dict(orgid=orgid))

    def get_relay(self, relayid):
        """Get relay settings"""
        return self.api_call(
            ENDPOINTS['relays']['get'],
            dict(relayid=relayid))

    def create_relay(self, orgid, data):
        """Create relay settings"""
        return self.api_call(
            ENDPOINTS['relays']['new'],
            dict(orgid=orgid), body=data)

    def update_relay(self, relayid, data):
        """Update relay settings"""
        return self.api_call(
            ENDPOINTS['relays']['update'],
            dict(relayid=relayid),
            body=data)

    def delete_relay(self, relayid, data):
        """Delete relay settings"""
        return self.api_call(
            ENDPOINTS['relays']['delete'],
            dict(relayid=relayid),
            body=data)

    def get_fallbackservers(self, orgid, page=None):
        """Get Fallback server"""
        opts = {}
        if page:
            opts['page'] = page
        return self.api_call(
            ENDPOINTS['fallbackservers']['list'],
            dict(orgid=orgid), **opts)

    def get_fallbackserver(self, serverid):
        """Get Fallback server"""
        return self.api_call(
            ENDPOINTS['fallbackservers']['get'],
            dict(serverid=serverid))

    def create_fallbackserver(self, orgid, data):
        """Create Fallback server"""
        return self.api_call(
            ENDPOINTS['fallbackservers']['new'],
            dict(orgid=orgid), body=data)

    def update_fallbackserver(self, serverid, data):
        """Update Fallback server"""
        return self.api_call(
            ENDPOINTS['fallbackservers']['update'],
            dict(serverid=serverid),
            body=data)

    def delete_fallbackserver(self, serverid, data):
        """Delete Fallback server"""
        return self.api_call(
            ENDPOINTS['fallbackservers']['delete'],
            dict(serverid=serverid),
            body=data)

    def get_org_smarthost(self, orgid, serverid):
        """Get an organization smarthost"""
        return self.api_call(
            ENDPOINTS['orgsmarthosts']['get'],
            dict(orgid=orgid, serverid=serverid))

    def create_org_smarthost(self, orgid, data):
        """Create an organization smarthost"""
        return self.api_call(
            ENDPOINTS['orgsmarthosts']['new'],
            dict(orgid=orgid),
            body=data)

    def update_org_smarthost(self, orgid, serverid, data):
        """Update an organization smarthost"""
        return self.api_call(
            ENDPOINTS['orgsmarthosts']['update'],
            dict(orgid=orgid, serverid=serverid),
            body=data)

    def delete_org_smarthost(self, orgid, serverid, data):
        """Delete an organization smarthost"""
        return self.api_call(
            ENDPOINTS['orgsmarthosts']['delete'],
            dict(orgid=orgid, serverid=serverid),
            body=data)

    def get_status(self):
        """Get system status"""
        return self.api_call(ENDPOINTS['status'])
