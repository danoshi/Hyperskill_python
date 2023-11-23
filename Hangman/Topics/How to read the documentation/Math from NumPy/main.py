# import the required library
import math


def calculate_cosine(angle_in_degrees):
    # do not forget to round the result and print it
    x = math.radians(angle_in_degrees)
    erg = math.cos(x)
    print(round(erg, 2))


