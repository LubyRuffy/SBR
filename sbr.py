from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
import RPi.GPIO as GPIO
from motor import MotorIf as Motor

# initial configuration
GPIO.setmode(GPIO.BOARD)
mL = Motor(33,35,37)

class SBRHandler(BaseHTTPRequestHandler):
    def setup(self):
        
        self.mL = Motor(33,35,37)
        self.mR = Motor(36,38,40)
        self.mL.set_direction('FORWARD')
        self.mR.set_direction('FORWARD')
        self.mR.set_speed(50)
        self.mL.set_speed(50)

    def __init__(self, *args, **kwargs):
        self.data = { 'status': 'ok' }
        self.setup()
        #super(SBRHandler, self).__init__(*args,**kwargs)

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
    GPIO.cleanup()
    pass

