import time
import board
import busio
import adafruit_mpr121
from adafruit_apds9960.apds9960 import APDS9960

# sensor - proximity
i2c1 = board.I2C()
apds = APDS9960(i2c1)
apds.enable_proximity = True

# sensor - capacitance touch
i2c2 = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c2)

while True:
    ########################################
    # sensor values
    PROXIMITY = apds.proximity
    CUR_TIME = time.strftime("%H:%M:%S")

    # constants
    HAND_DISTANCE_CLOSE = 10
    PAUSE_BUTTON = 1
    START_BUTTON = 4
    ########################################

    # detect hand proximity
    if PROXIMITY > HAND_DISTANCE_CLOSE:
        print("Hand is close! " + CUR_TIME)

    # detect touch sensor activation
    for i in range(12):
        if mpr121[i].value:
            if i == PAUSE_BUTTON:
                print("Pause Button Pressed!")
            elif i == START_BUTTON:
                print("Start Button Pressed!")

    # sleep time
    time.sleep(0.2)

