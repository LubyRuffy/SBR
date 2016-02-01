from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import os
serv = HTTPServer(("",8080),SimpleHTTPRequestHandler)
serv.serve_forever()
