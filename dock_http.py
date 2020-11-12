#!/usr/bin/python3
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os

hostName = ""
hostPort = 8086


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        header = """<HEAD><TITLE>Test Page</TITLE></HEAD>\n<BODY><TABLE><TR><TH>VARIABLE</TH><TH>VALUE</TH></TR>\n"""
        out_html = header
        for head in self.headers:
            out_html = out_html + f"<TR><TD>{head}</TD><TD>{self.headers[head]}</TD></TR>\n"
        out_html = out_html + f"<TR><TD>Path</TD><TD>{self.path}</TD></TR>\n"
        for l in os.environ:
            out_html = out_html + f"<TR><TD>{l}</TD><TD>{os.environ[l]}</TD></TR>\n"
        out_html = out_html + """</TABLE></BODY>\n"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(out_html, 'utf-8'))

    def do_POST(self):
        print("incomming http: ", self.path)

        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        try:
            print(str(post_data))
        except (RuntimeError, TypeError, NameError):
            pass
        self.send_response(200)


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
