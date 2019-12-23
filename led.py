from machine import Pin, PWM
colors = {"green":[0, 5, 0], "blue":[0, 0, 5], "red":[5, 0, 0]} # And others...

try:
    from config import LED_Pins
    red = PWM(Pin(LED_Pins['r']))
    green = PWM(Pin(LED_Pins['g']))
    blue = PWM(Pin(LED_Pins['b']))
except:
    red = PWM(Pin(13))
    green = PWM(Pin(14))
    blue = PWM(Pin(12))

def rgb_color(**kwargs):    
    if "r" in **kwargs:
        red.duty(int(**kwargs["r"]))
    if "g" in **kwargs:
        green.duty(int(**kwargs["g"]))
    if "b" in **kwargs:
        blue.duty(int(**kwargs["b"]))
    if "color" in **kwargs:
        if **kwargs["color"] in colors:
            r = colors[**kwargs["color"]][0]
            g = colors[**kwargs["color"]][1]
            b = colors[**kwargs["color"]][2]
            red.duty(r)
            green.duty(g)
            blue.duty(b)
        elif **kwargs["color"] == None:
            red.duty(0)
            green.duty(0)
            blue.duty(0)
            
