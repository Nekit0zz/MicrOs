# gui

from machine import ADC, PWM, Pin, I2C
import network
import time
import config
import ssd1306
import button
import network

i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = config.oled_width
oled_height = config.oled_height
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

"""
oled.text(text, x, y, color) 1 = white 0 = black
oled.fill(1 or 0)
oled.pixel(x, y, color)
oled.invert(True or False)
oled.scroll(dx, dy)
oled.show()
"""
sta_if = network.WLAN(network.STA_IF)
def main():
    a0 = ADC(0)
    oled.text("Button " + str(button.butt()), 0, 0, 1)
    oled.text(sta_if.ifconfig()[0], 0, 20, 1)
    oled.text(str(a0.read()), 0, 40, 1)
    oled.show()
    time.sleep(0.2)
    oled.fill(0)
