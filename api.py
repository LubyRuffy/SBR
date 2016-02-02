from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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

motors = {}
gyroState = {}

class MotorMgr(Resource):
    def get(self, motor, speed):
        return {todo_id: todos[todo_id]}

    def put(self, motor, speed):
        motors[motor] = request.form['speed']
        return {todo_id: todos[todo_id]}

api.add_resource(MotorMgr, '/<string:motor>/<int:speed>')

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()

