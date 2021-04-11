import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


keyboard = Keyboard(usb_hid.devices)

for i in range(1,10) :
    keyboard.send(Keycode.LEFT_ARROW)
    time.sleep(0.5)
keyboard.send(Keycode.ENTER)

    
