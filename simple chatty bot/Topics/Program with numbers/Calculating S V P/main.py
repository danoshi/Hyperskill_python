# put your python code here
length = int(input())
width = int(input())
height = int(input())

a = 4
b = 2

all_edges = a * (length + width + height)
surface_area = b * ((length * width)
                    + (width * height)
                    + (length * height))
volume = (length * width * height)
print(all_edges)
print(surface_area)
print(volume)
