# -*- coding: utf-8 -
#
# Copyright (c) 2008 (c) Benoit Chesneau <benoitc@e-engura.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
"""HTTP test server"""
import os
import json
import threading

from urllib import unquote
from urlparse import urlparse
from urlparse import parse_qsl, parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from restkit.util import to_bytestring


HOST = 'localhost'
PORT = (os.getpid() % 31000) + 1024
TOKEN = '6e2347bc-278e-42f6-a84b-fa1766140cbd'


class HTTPTestHandler(BaseHTTPRequestHandler):
    """Testing handler"""
    def __init__(self, request, client_address, server):
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def _check_token(self):
        if 'Authorization' not in self.headers or \
                self.headers['Authorization'] != 'Bearer %s' % TOKEN:
            self.send_error(401)

    def do_GET(self):
        self._check_token()
        self.parsed_uri = urlparse(unquote(self.path))
        self.query = {}
        for key, val in parse_qsl(self.parsed_uri[4]):
            self.query[key] = val.decode('utf-8')
        path = self.parsed_uri[2]
        extra_headers = [('Content-type', 'application/json')]

        if path in [
            '/api/v1/status',
            '/api/v1/relays/1',
            '/api/v1/organizations/1',
            '/api/v1/organizations',
            '/api/v1/radiussettings/1/2/3',
            '/api/v1/ldapsettings/1/2/3',
            '/api/v1/authservers/9/4',
            '/api/v1/authservers/9',
            '/api/v1/deliveryservers/9/4',
            '/api/v1/deliveryservers/9',
            '/api/v1/domainaliases/9',
            '/api/v1/domainaliases/9/4',
            "/api/v1/users",
            '/api/v1/users/5',
            '/api/v1/aliasaddresses/2',
            '/api/v1/domains',
            '/api/v1/domains/1',
                '/api/v1/domains/byname/example.com']:
            with open('tests%s.json' % path) as handle:
                data = handle.read()
            self._respond(200, extra_headers, data)
        else:
            self._respond(404, [('Content-type', 'text/plain')], "Not Found")

    def do_POST(self):
        self._check_token()
        self.parsed_uri = urlparse(self.path)
        self.query = {}
        for key, val in parse_qsl(self.parsed_uri[4]):
            self.query[key] = val.decode('utf-8')
        path = self.parsed_uri[2]
        extra_headers = [('Content-type', 'application/json')]

        if path == '/api/v1/users':
            content_length = int(self.headers.get('Content-length', 0))
            body = self.rfile.read(content_length)
            form = parse_qs(body)
            if 'username' in form and 'email' in form and 'password2' in form:
                resp = {}
                for item in form:
                    if item in ['password1', 'password2']:
                        continue
                    resp[item] = form[item][0]
                resp['id'] = 10
                self._respond(201, extra_headers, json.dumps(resp))
        elif path == '/api/v1/users/chpw/10':
            content_length = int(self.headers.get('Content-length', 0))
            body = self.rfile.read(content_length)
            form = parse_qs(body)
            if 'password1' in form and 'password2' in form:
                self._respond(204, extra_headers, "")
        elif path in [
            '/api/v1/relays/1',
            '/api/v1/organizations',
            '/api/v1/radiussettings/1/2',
            '/api/v1/ldapsettings/1/2',
            '/api/v1/authservers/3',
            '/api/v1/authservers/9',
            '/api/v1/deliveryservers/9',
            '/api/v1/domainaliases/9',
            '/api/v1/aliasaddresses/2',
                '/api/v1/domains']:
            content_length = int(self.headers.get('Content-length', 0))
            body = self.rfile.read(content_length)
            form = parse_qs(body)
            resp = {}
            for item in form:
                resp[item] = form[item][0]
            resp['id'] = 3
            self._respond(201, extra_headers, json.dumps(resp))
        else:
            self._respond(404, [('Content-type', 'text/plain')], "Not Found")

    def do_PUT(self):
        self._check_token()
        self.parsed_uri = urlparse(self.path)
        self.query = {}
        for key, val in parse_qsl(self.parsed_uri[4]):
            self.query[key] = val.decode('utf-8')
        path = self.parsed_uri[2]
        extra_headers = [('Content-type', 'application/json')]
        if path == '/api/v1/users':
            content_length = int(self.headers.get('Content-length', 0))
            body = self.rfile.read(content_length)
            form = parse_qs(body)
            if 'username' in form and 'email' in form and 'password2' in form:
                resp = {}
                for item in form:
                    if item in ['password1', 'password2']:
                        continue
                    resp[item] = form[item][0]
                resp['id'] = 10
                self._respond(201, extra_headers, json.dumps(resp))
        elif path in [
            '/api/v1/relays/1',
            '/api/v1/organizations/1',
            '/api/v1/radiussettings/1/2/3',
            '/api/v1/ldapsettings/1/2/3',
            '/api/v1/authservers/9/3',
            '/api/v1/deliveryservers/9/4',
            '/api/v1/domainaliases/9/3',
            '/api/v1/aliasaddresses/3',
                '/api/v1/domains/3']:
            content_length = int(self.headers.get('Content-length', 0))
            body = self.rfile.read(content_length)
            form = parse_qs(body)
            resp = {}
            for item in form:
                resp[item] = form[item][0]
            resp['id'] = 3
            self._respond(200, extra_headers, json.dumps(resp))
        else:
            self._respond(404, [('Content-type', 'text/plain')], "Not Found")

    def do_DELETE(self):
        self._check_token()
        if self.path in [
            "/api/v1/relays/1",
            "/api/v1/organizations/1",
            "/api/v1/radiussettings/1/2/3",
            "/api/v1/ldapsettings/1/2/3",
            "/api/v1/authservers/9/3",
            "/api/v1/deliveryservers/9/4",
            "/api/v1/domainaliases/9/3",
            "/api/v1/domains/3",
            "/api/v1/users/10",
                "/api/v1/aliasaddresses/3"]:
            extra_headers = [('Content-type', 'text/plain')]
            self._respond(204, extra_headers, '')
        else:
            self.error_Response()

    def error_Response(self, message=None):
        req = [
            ('HTTP method', self.command),
            ('path', self.path),
            ]
        if message:
            req.append(('message', message))

        body_parts = ['Bad request:\r\n']
        for key, val in req:
            body_parts.append(' %s: %s\r\n' % (key, val))
        body = ''.join(body_parts)
        self._respond(
            400,
            [
                ('Content-type', 'text/plain'),
                ('Content-Length', str(len(body)))
            ],
            body)

    def _respond(self, http_code, extra_headers, body):
        self.send_response(http_code)
        keys = []
        for key, val in extra_headers:
            self.send_header(key, val)
            keys.append(key)
        if body:
            body = to_bytestring(body)
        self.end_headers()
        self.wfile.write(body)
        self.wfile.close()

    def finish(self):
        if not self.wfile.closed:
            self.wfile.flush()
        self.wfile.close()
        self.rfile.close()


server_thread = None


def run_server_test():
    global server_thread
    if server_thread is not None:
        return
    server = HTTPServer((HOST, PORT), HTTPTestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
