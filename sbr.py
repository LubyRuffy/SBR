from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class SBRHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200,"OK")
        self.send_header('content-type','text/plain')
        self.end_headers()
        self.wfile.write("""<HTML>
        <HEAD><TITLE></TITLE></HEAD>
        <BODY>Hello</BODY>
        </HTML>
        """)
        pass
    def do_POST(self):
        pass
    def do_PUT(self):
        pass
serv = HTTPServer(("",8080),SimpleHTTPRequestHandler)
serv.serve_forever()
