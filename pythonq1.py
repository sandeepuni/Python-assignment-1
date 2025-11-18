# -*- coding: utf-8 -*-

distance = int(input("How far do you want to travel (in miles)? "))

if distance < 3:
    print("You should ride a Bicycle.")
elif distance>=3 and distance < 300:
    print("You should ride a Motor-Cycle.")
else:
    print("You should drive a Super-Car.")
