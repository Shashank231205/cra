# data/utils/robo_controller.py
import serial

# Connect to Arduino/Controller
def trigger_motor(action):
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    action_map = {
        "conductor": "A",
        "insulator": "B",
        "semiconductor": "C"
    }
    if action in action_map:
        ser.write(action_map[action].encode())
    ser.close()
