import time
import board
import neopixel
from digitalio import DigitalInOut, Pull

led = neopixel.NeoPixel(board.NEOPIXEL, 1) # For working with the LED

button = DigitalInOut(board.SWITCH)
button.switch_to_input(pull=Pull.DOWN)
button_state = False

time.sleep(1)
led.fill((0, 0, 255))

while True:
    if button.value and not button_state:
        led.fill((255, 0, 0))
        print("Pressing button")
        button_state = True

    if not button.value and button_state:
        led.fill((0, 0, 255))
        print("Released button")
        button_state = False




