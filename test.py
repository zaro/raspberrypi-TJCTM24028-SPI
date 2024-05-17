#!/usr/bin/env python
import time
import busio
import digitalio
from board import SCK, MOSI, MISO, CE0, D24, D25

from adafruit_rgb_display import color565
import adafruit_rgb_display.ili9341 as ili9341

from PIL import Image, ImageDraw
import random



# Configuration for CS and DC pins:
CS_PIN = CE0
DC_PIN = D25
RESET_PIN = D24
BAUDRATE = 24000000


# Setup SPI bus using hardware SPI:
spi = busio.SPI(clock=SCK, MOSI=MOSI, MISO=MISO)

# Create the ILI9341 display:
display = ili9341.ILI9341(spi, cs=digitalio.DigitalInOut(CS_PIN),
                               dc=digitalio.DigitalInOut(DC_PIN),
                          rst=digitalio.DigitalInOut(RESET_PIN),
                               baudrate=BAUDRATE)


image = Image.open("food.png")
images = []
for x in range(0,5):
    for y in range(0,4):
        images.append( image.crop((x*32,y*32,(x+1)*32,(y+1)*32)) )

count1 = 0
count2 = 0
t = time.time()
# Main loop:
while True:
    # Clear the display
    #display.fill(0)
    # Draw a red pixel in the center.
    #display.pixel(120, 160, color565(255, 0, 0))
    for x in range(0,5):
        for y in range(0,4):
            display.image(images[y*5 + x], 0, x*32,y*32)
    # Pause 2 seconds.
   # time.sleep(2)
    # Clear the screen blue.
    #display.fill(color565(0, 0, 255))
    # Pause 2 seconds.
    #time.sleep(2)
    count2 += 1

    dt = time.time() - t
    if  dt >= 3.0:
        print("Current FPS: ", round((count2-count1)/dt, 3))
        t = time.time()
        count1  =count2

