from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
import RPi.GPIO as GPIO

class MotorMgr(object):
    def __init__(fwdPin,revPin,speed):
        self = {}
        self['fwdPin'] = fwdPin
        self['revPin'] = revPin
        
    def set_speed(self, speed):
        self.set_rspeed(speed)
        self.set_lspeed(speed)
        pass
    
    def set_rspeed(self,speed):
        self['rspeed'] = speed
        pass
    
    def set_lspeed(self,speed):
        self['lspeed'] = speed
        pass
    
class SBRHandler(BaseHTTPRequestHandler, object):
    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        
    def __init__(self, *args, **kwargs):
        self.data = { 'status': 'ok' }
        super(SBRHandler, self).__init__(*args,**kwargs)


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

try:    
    serv = HTTPServer(("",8080),SBRHandler)
    serv.serve_forever()
except KeyboardInterrupt:
    pass

