from math import sin
from math import cos
from math import radians

num = int(input())
deg = radians(num)

cos = cos(deg)
sin = sin(deg)

erg = round(cos / sin, 10)

print(erg)
