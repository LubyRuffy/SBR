from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json

class SBRHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200,"OK")
        self.send_header('content-type','text/json')
        self.end_headers()
        self.wfile.write("""{
        "status" : "ok"
        }""")
        pass
    def do_POST(self):
        pass
    def do_PUT(self):
        pass
serv = HTTPServer(("",8080),SBRHandler)
serv.serve_forever()
