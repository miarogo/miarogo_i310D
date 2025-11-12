# -*- coding: utf-8 -*-
import math

def calculate_volume_of_sphere(radius):
    if radius < 0:
        raise ValueError("radius can't be negative.")
    volume = (4/3) * math.pi * (radius ** 3)
    return volume
print(calculate_volume_of_sphere(30))
print (calculate_volume_of_sphere(40))
