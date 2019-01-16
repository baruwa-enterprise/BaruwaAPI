# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# BaruwaAPI Python bindings for Baruwa REST API
# Copyright (C) 2015-2019 Andrew Colin Kissa <andrew@topdog.za.net>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""
BaruwaAPI Endpoints
"""

ENDPOINTS = {
    "users": {
        "list": {"name": "/users", "method": "GET"},
        "new": {"name": "/users", "method": "POST"},
        "get": {"name": "/users/%(userid)s", "method": "GET"},
        "update": {"name": "/users", "method": "PUT"},
        "delete": {"name": "/users/%(userid)s", "method": "DELETE"},
        "password": {"name": "/users/chpw/%(userid)s", "method": "POST"}
    },
    "aliases": {
        "get": {"name": "/aliasaddresses/%(addressid)s", "method": "GET"},
        "new": {"name": "/aliasaddresses/%(userid)s", "method": "POST"},
        "update": {
            "name": "/aliasaddresses/%(addressid)s",
            "method": "PUT"},
        "delete": {
            "name": "/aliasaddresses/%(addressid)s",
            "method": "DELETE"}
    },
    "domains": {
        "list": {"name": "/domains", "method": "GET"},
        "new": {"name": "/domains", "method": "POST"},
        "get": {"name": "/domains/%(domainid)s", "method": "GET"},
        "get_by_name": {
            "name": "/domains/byname/%(domainname)s",
            "method": "GET"},
        "update": {"name": "/domains/%(domainid)s", "method": "PUT"},
        "delete": {"name": "/domains/%(domainid)s", "method": "DELETE"}
    },
    "domainaliases": {
        "list": {"name": "/domainaliases/%(domainid)s", "method": "GET"},
        "new": {"name": "/domainaliases/%(domainid)s", "method": "POST"},
        "get": {
            "name": "/domainaliases/%(domainid)s/%(aliasid)s",
            "method": "GET"},
        "update": {
            "name": "/domainaliases/%(domainid)s/%(aliasid)s",
            "method": "PUT"},
        "delete": {
            "name": "/domainaliases/%(domainid)s/%(aliasid)s",
            "method": "DELETE"}
    },
    "deliveryservers": {
        "list": {"name": "/deliveryservers/%(domainid)s", "method": "GET"},
        "new": {"name": "/deliveryservers/%(domainid)s", "method": "POST"},
        "get": {
            "name": "/deliveryservers/%(domainid)s/%(serverid)s",
            "method": "GET"},
        "update": {
            "name": "/deliveryservers/%(domainid)s/%(serverid)s",
            "method": "PUT"},
        "delete": {
            "name": "/deliveryservers/%(domainid)s/%(serverid)s",
            "method": "DELETE"}
    },
    "userdeliveryservers": {
        "list": {"name": "/userdeliveryservers/%(domainid)s", "method": "GET"},
        "new": {"name": "/userdeliveryservers/%(domainid)s", "method": "POST"},
        "get": {
            "name": "/userdeliveryservers/%(domainid)s/%(serverid)s",
            "method": "GET"},
        "update": {
            "name": "/userdeliveryservers/%(domainid)s/%(serverid)s",
            "method": "PUT"},
        "delete": {
            "name": "/userdeliveryservers/%(domainid)s/%(serverid)s",
            "method": "DELETE"}
    },
    "domainsmarthosts": {
        "list": {"name": "/domains/smarthosts/%(domainid)s", "method": "GET"},
        "new": {"name": "/domains/smarthosts/%(domainid)s", "method": "POST"},
        "get": {
            "name": "/domains/smarthosts/%(domainid)s/%(serverid)s",
            "method": "GET"},
        "update": {
            "name": "/domains/smarthosts/%(domainid)s/%(serverid)s",
            "method": "PUT"},
        "delete": {
            "name": "/domains/smarthosts/%(domainid)s/%(serverid)s",
            "method": "DELETE"}
    },
    "authservers": {
        "list": {"name": "/authservers/%(domainid)s", "method": "GET"},
        "new": {"name": "/authservers/%(domainid)s", "method": "POST"},
        "get": {
            "name": "/authservers/%(domainid)s/%(serverid)s",
            "method": "GET"},
        "update": {
            "name": "/authservers/%(domainid)s/%(serverid)s",
            "method": "PUT"},
        "delete": {
            "name": "/authservers/%(domainid)s/%(serverid)s",
            "method": "DELETE"}
    },
    "ldapsettings": {
        "new": {
            "name": "/ldapsettings/%(domainid)s/%(serverid)s",
            "method": "POST"},
        "get": {
            "name": "/ldapsettings/%(domainid)s/%(serverid)s/%(settingsid)s",
            "method": "GET"},
        "update": {
            "name": "/ldapsettings/%(domainid)s/%(serverid)s/%(settingsid)s",
            "method": "PUT"},
        "delete": {
            "name": "/ldapsettings/%(domainid)s/%(serverid)s/%(settingsid)s",
            "method": "DELETE"}
    },
    "radiussettings": {
        "new": {
            "name": "/radiussettings/%(domainid)s/%(serverid)s",
            "method": "POST"},
        "get": {
            "name": "/radiussettings/%(domainid)s/%(serverid)s/%(settingsid)s",
            "method": "GET"},
        "update": {
            "name": "/radiussettings/%(domainid)s/%(serverid)s/%(settingsid)s",
            "method": "PUT"},
        "delete": {
            "name": "/radiussettings/%(domainid)s/%(serverid)s/%(settingsid)s",
            "method": "DELETE"}
    },
    "organizations": {
        "list": {"name": "/organizations", "method": "GET"},
        "new": {"name": "/organizations", "method": "POST"},
        "get": {"name": "/organizations/%(orgid)s", "method": "GET"},
        "update": {"name": "/organizations/%(orgid)s", "method": "PUT"},
        "delete": {"name": "/organizations/%(orgid)s", "method": "DELETE"}
    },
    "relays": {
        "new": {"name": "/relays/%(orgid)s", "method": "POST"},
        "get": {"name": "/relays/%(relayid)s", "method": "GET"},
        "update": {"name": "/relays/%(relayid)s", "method": "PUT"},
        "delete": {"name": "/relays/%(relayid)s", "method": "DELETE"}
    },
    "fallbackservers": {
        "list": {"name": "/fallbackservers/list/%(orgid)s", "method": "GET"},
        "new": {"name": "/fallbackservers/%(orgid)s", "method": "POST"},
        "get": {"name": "/fallbackservers/%(serverid)s", "method": "GET"},
        "update": {"name": "/fallbackservers/%(serverid)s", "method": "PUT"},
        "delete": {
            "name": "/fallbackservers/%(serverid)s", "method": "DELETE"},
    },
    "orgsmarthosts": {
        "list": {"name": "/organizations/smarthosts/%(orgid)s", "method": "GET"},
        "new": {"name": "/organizations/smarthosts/%(orgid)s", "method": "POST"},
        "get": {
            "name": "/organizations/smarthosts/%(orgid)s/%(serverid)s",
            "method": "GET"},
        "update": {
            "name": "/organizations/smarthosts/%(orgid)s/%(serverid)s",
            "method": "PUT"},
        "delete": {
            "name": "/organizations/smarthosts/%(orgid)s/%(serverid)s",
            "method": "DELETE"}
    },
    "status": {"name": "/status", "method": "GET"}
}
