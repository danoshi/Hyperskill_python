# put your python code here
duration = int(input())
food_day = int(input())
flight_cost = int(input())
one_night_hotel = int(input())

total_food = duration * food_day
total_hotel = (duration - 1) * one_night_hotel
total_flight = flight_cost * 2

erg = total_flight + total_hotel + total_food

print(erg)
