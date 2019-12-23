# buttons

from machine import ADC, Pin


def butt():
    a0 = ADC(0)
    if a0.read() > 472 and a0.read() < 476:
        return 1
    elif a0.read() > 485 and a0.read() < 490:
        return 2
    elif a0.read() > 499 and a0.read() < 503:
        return 3
    elif a0.read() > 514 and a0.read() < 518:
        return 4
    elif a0.read() > 530 and a0.read() < 536:
        return 5
    else:
        return 0
    
