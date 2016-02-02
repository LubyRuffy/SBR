from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json

class SBRHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super(SBRHandler, BaseHTTPRequestHandler(*args,**kwargs))
        self.data = {}
        
    def do_GET(self):
        self.send_response(200,"OK")
        self.send_header('content-type','text/json')
        self.end_headers()
        self.wfile.write(json.dumps(self.data))
        pass
    
    def do_POST(self):
        pass
    def do_PUT(self):
        pass
serv = HTTPServer(("",8080),SBRHandler)
serv.serve_forever()
