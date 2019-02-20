# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# BaruwaAPI Python bindings for Baruwa REST API
# Copyright (C) 2015-2019 Andrew Colin Kissa <andrew@topdog.za.net>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""
BaruwaAPI
"""
from BaruwaAPI.resource import BaruwaAPIClient

# pylint: disable=invalid-name
version_info = (0, 0, 5)
__author__ = "Andrew Colin Kissa"
__copyright__ = u"© 2015-2019 Andrew Colin Kissa"
__email__ = "andrew@topdog.za.net"
__version__ = ".".join(map(str, version_info))


assert BaruwaAPIClient
