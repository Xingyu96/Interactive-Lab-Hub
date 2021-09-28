import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Lab 2.ii 2nd screen control
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

while True:
    # Draw a black filled box to clear the image.
    # draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
    
    # emojis
    white_circle = u"\u26AA"
    fill_circle = u"\u26AB"
    person = u"\u26A1"
    peace = u"\u262E"

    separator = "<======= " + peace + " =======>"
    
    # time
    clock_title = "<=== CIRCLE HOURS ===>"
    CUR_TIME = time.strftime("%H:%M:%S")
    time_list = CUR_TIME.split(":")
    
    hours = int(time_list[0])
    minutes = time_list[1]
    seconds = int(time_list[2])
    
    if buttonB.value and not buttonA.value:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        
        clock_date_title = "<=== CIRCLE DATES ===>"

        # current date
        cur_month = time.strftime("%-m")
        cur_day = time.strftime("%d")
        cur_weekday = time.strftime("%w")
        
        # month row
        month_string = ""

        for i in range(12):
            if i < int(cur_month):
                month_string += fill_circle
            else:
                month_string += white_circle

        day_string = ""

        for i in range(3):
            if i < int(cur_day[0]):
                day_string += fill_circle
            else:
                day_string += white_circle
        day_string += "|"
        for i in range(10):
            if i < int(cur_day[1]):
                day_string += fill_circle
            else:
                day_string += white_circle

        # draw clock date screen
        y = top

        # clock title
        draw.text((x, y), clock_date_title, font=font, fill="#FFFFFF")
        y += font.getsize(clock_date_title)[1]

        # month row
        draw.text((x, y), month_string, font=font, fill="#3FC059")
        y += font.getsize(month_string)[1]
        y += font.getsize(month_string)[1]

        draw.text((x, y), day_string, font=font, fill="#4083BF")

        #display.fill(color565(0,255,0))
        disp.image(image, rotation)

    elif buttonA.value and buttonB.value:

        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # hours rows
        twelve_circles = [white_circle for x in range(12)]
        am_string = ""
        pm_string = ""

        for i in range(12):
            if (i < hours):
                am_string += fill_circle
            else:
                am_string += white_circle

        for i in range(12, 24):
            if (i < hours):
                pm_string += fill_circle
            else:
                pm_string += white_circle

        # minutes row
        minutes_string = ""
        minutes_ten = int(minutes[0])
        minutes_digit = int(minutes[1])

        for i in range(5):
            if (i < minutes_ten):
                minutes_string += fill_circle
            else:
                minutes_string += white_circle

        minutes_string += " | "

        for i in range(10):
            if (i < minutes_digit):
                minutes_string += fill_circle
            else:
                minutes_string += white_circle
        
        # seconds row
        seconds_string = ""
        
        for i in range(1, 4):
            if i * 5 <= seconds:
                seconds_string += fill_circle
            else:
                seconds_string += white_circle
        
        seconds_string += " | "

        for i in range(4, 7):
            if i * 5 <= seconds:
                seconds_string += fill_circle
            else:
                seconds_string += white_circle

        seconds_string += " | "

        for i in range(7, 10):
            if i * 5 <= seconds:
                seconds_string += fill_circle
            else:
                seconds_string += white_circle

        seconds_string += " | "

        for i in range(10, 13):
            if i * 5 <= seconds:
                seconds_string += fill_circle
            else:
                seconds_string += white_circle


        y = top
        # clock title
        draw.text((x, y), clock_title, font=font, fill="#FFFFFF")
        y += font.getsize(clock_title)[1]
        
        # am row
        draw.text((x, y), am_string, font=font, fill="#FFA500")
        y += font.getsize(am_string)[1]
        
        # pm row
        draw.text((x, y), pm_string, font=font, fill="#4083BF")
        y += font.getsize(pm_string)[1]
        
        draw.text((x, y), separator, font=font, fill="#FFFFFF")
        y += font.getsize(separator)[1]

        # minutes row
        draw.text((x, y), minutes_string, font=font, fill="#3FC059")
        y += font.getsize(minutes_string)[1]

        draw.text((x, y), separator, font=font, fill="#FFFFFF")
        y += font.getsize(separator)[1]

        # seconds row
        draw.text((x, y), seconds_string, font=font, fill="#974DB2")
        y += font.getsize(seconds_string)[1]

        draw.text((x, y), separator, font=font, fill="#FFFFFF")

        # Display image.
        disp.image(image, rotation)
        time.sleep(1)
