# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import uos, machine, network, time
from machine import PWM, Pin, I2C
import gui
import gc
import webrepl
import config
import ssd1306

"""
fix if boot file brokem:
import network, webrepl, config
webrepl.start()
sta_if = network.WLAN(network.STA_IF)
sta_if.connect(config.HOME_WIFI, config.HOME_PASSWORD)
"""

blue = PWM(Pin(14))
green = PWM(Pin(12))
green.duty(0)
blue.duty(1)

i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = config.oled_width
oled_height = config.oled_height
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text("Loading MicroS", 0, 0, 1)
oled.show()

try:
    import led
except:
    pass

webrepl.start()
gc.collect()

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(config.HOME_WIFI, config.HOME_PASSWORD)
        i = 0
        while not sta_if.isconnected() and i < 5:
            time.sleep(2)
        if sta_if.isconnected():
            print('network config:', sta_if.ifconfig())
            oled.text("Loading MicroS", 0, 0, 1)
            oled.text("Wifi connected!", 0, 30, 1)
            oled.show()
            for i in range(20):
                green.duty(i)
                time.sleep(0.1)
            for i in range(20):
                green.duty(20-i)
                time.sleep(0.1)
        else:
            sta_if.connect(config.MOBILE_WIFI, config.MOBILE_PASSWORD)
            i = 0
            while not sta_if.isconnected() and i < 5:
                time.sleep(2)
            if sta_if.isconnected():
                print('network config:', sta_if.ifconfig())
                for i in range(20):
                    green.duty(i)
                    time.sleep(0.1)
                for i in range(20):
                    green.duty(20-i)
                    time.sleep(0.1)
    
do_connect()

while True:
    gui.main()
