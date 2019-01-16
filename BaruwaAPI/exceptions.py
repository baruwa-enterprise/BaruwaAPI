# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# BaruwaAPI Python bindings for Baruwa REST API
# Copyright (C) 2015-2019 Andrew Colin Kissa <andrew@topdog.za.net>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""
BaruwaAPI exceptions
"""


class BaruwaAPIError(Exception):
    """BaruwaAPI Exceptions"""
    def __init__(self, code, message):
        """Init"""
        super(BaruwaAPIError, self).__init__(message)
        self.code = code
