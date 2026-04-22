from machine import Pin
import time


red = Pin(13, Pin.OUT)
yellow = Pin(15, Pin.OUT)
green = Pin(14, Pin.OUT)


def all_off():
    red.value(0)
    yellow.value(0)
    green.value(0)

while True:
    # Đèn đỏ 5 giây
    all_off()
    red.value(1)
    print('ĐỎ — Dừng')
    time.sleep(5)


    # Đèn xanh 5 giây
    all_off()
    green.value(1)
    print('XANH — Đi')
    time.sleep(5)


    # Đèn vàng 2 giây
    all_off()
    yellow.value(1)
    print('VÀNG — Chuẩn bị dừng')
    time.sleep(2)

