from flask import Flask, request, Response
from flask_restful import Resource, Api

import json
import RPi.GPIO as GPIO
from motor import MotorIf as Motor
from accelerometer import Accelerometer as A

# initial configuration
GPIO.setmode(GPIO.BOARD)
mL = Motor(33,35,37)
mR = Motor(36,38,40)
mL.set_direction('FORWARD')
mR.set_direction('FORWARD')
mR.set_speed(50)
mL.set_speed(50)
acc = A(0x68)

motors = {'L': {'speed': 0 , 'dir': 'FORWARD' },
          'R': {'speed': 0 , 'dir': 'FORWARD' } }


class MotorMgr(Resource):
    def get(self, motor):
        return Response(json.dumps(motors[motor]),mimetype='text/json')

    def put(self, motor):
        speed = request.form['speed']
        dir = request.form['dir']
        if speed:
            motors[motor]['speed'] = speed
        if dir:
            motors[motor]['dir'] = dir
        return json.dumps(motors)

class GyroMgr(Resource):
    def get(self):
        pass        

if __name__ == '__main__':
    try:
        app = Flask(__name__)
        api = Api(app)
        api.add_resource(MotorMgr, '/motor/<string:motor>')
        api.add_resource(GyroMgr, '/gyro')
        app.run(host='0.0.0.0', debug=True)
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()
