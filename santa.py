import random
import os
from papirus import PapirusImage
from gpiozero import Button, PWMLED, LED

randomfile=""

button = Button(27)
led = PWMLED(22)
folder = 'santa/'
image = PapirusImage()

while True:
    button.wait_for_press()
    led.pulse(n=3)
    randomfile = random.sample(os.listdir("santa/"), 1)[0]
    image.write(folder + randomfile)
