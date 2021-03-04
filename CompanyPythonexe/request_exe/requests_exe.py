#!/usr/bin/env python
# -*- coding:utf-8 -*-
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 80

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write("<html>hello</html>")

def run_server():
    server = HTTPServer((HOST, PORT), RequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    # redirect www.x.x.x to 127.0.0.1 in hosts
    run_server()