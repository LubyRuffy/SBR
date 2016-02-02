from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
import RPi.GPIO as GPIO
from motor import MotorIf as Motor

# initial configuration
GPIO.setmode(GPIO.BOARD)
mL = Motor(33,35,37)
mR = Motor(36,38,40)
mL.set_direction('FORWARD')
mR.set_direction('FORWARD')
mR.set_speed(50)
mL.set_speed(50)

class SBRHandler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.data = { 'status': 'ok' }
        self.setup()
        super(SBRHandler, self).__init__(*args,**kwargs)

    def do_GET(self):
        self.send_response(200,"OK")
        self.send_header('content-type','text/json')
        self.end_headers()
        self.wfile.write(json.dumps(self.data))
        print json.dumps(self.data) 
        pass
    
    def do_POST(self):
        pass
    def do_PUT(self):
        pass

try:
    serv = HTTPServer(("",8080),SBRHandler)
    serv.serve_forever()
except KeyboardInterrupt:
    pass

print 'cleaning up'
GPIO.cleanup()
