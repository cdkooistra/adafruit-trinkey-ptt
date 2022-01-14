import time
import board
import neopixel
import usb_hid
from digitalio import DigitalInOut, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Create led object and give program rest time
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
time.sleep(0.5)

# Create keyboard object
kbd = Keyboard(usb_hid.devices)

# Button logistics
button = DigitalInOut(board.SWITCH)
button.switch_to_input(pull=Pull.DOWN)
button_state = False

# Fill the led with blue color
led.fill((0, 0, 255))

# Methods for pressing/releasing the button
def pressed():
    led.fill((255, 0, 0))
    # By default press T to use the button, can change to whatever button prefered
    kbd.press(Keycode.T)
    
def released():
    led.fill((0, 0, 255))
    # Release the configured button
    kbd.release(Keycode.T)

# Main loop for the controller
while True:
    if button.value and not button_state:
        pressed()
        button_state = True

    if not button.value and button_state:
        released()
        button_state = False

