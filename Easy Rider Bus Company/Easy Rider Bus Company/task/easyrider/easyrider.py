import json
import re
from datetime import datetime

def get_route_dictionary(json_data):
    route_dict = {}
    for item in json_data:
        bus_id = item['bus_id']
        stop_name = item['stop_name']
        stop_type = item['stop_type']
        route_dict.setdefault(bus_id, {'start': '', 'finish': '', 'stops': set()})
        route_dict[bus_id]['stops'].add(stop_name)
        if stop_type == 'S':
            if route_dict[bus_id]['start'] != '':
                return bus_id
            else:
                route_dict[bus_id]['start'] = stop_name
        if stop_type == 'F':
            if route_dict[bus_id]['finish'] != '':
                return bus_id
            else:
                route_dict[bus_id]['finish'] = stop_name
    return route_dict


def process_route_dictionary(route_dict):
    start_stops = set()
    transfer_stops = set()
    finish_stops = set()
    list_of_routes = list(route_dict.keys())
    while list_of_routes:
        test_item = list_of_routes.pop()
        if route_dict[test_item]['start'] == '' or route_dict[test_item]['finish'] == '':
            print(f'There is no start or end stop for the line: {test_item}.')
            return False
        start_stops.add(route_dict[test_item]['start'])
        finish_stops.add(route_dict[test_item]['finish'])
        for route in list_of_routes:
            transfer_stops.update(route_dict[test_item]['stops'].intersection(route_dict[route]['stops']))
    start_stops = sorted(list(start_stops))
    transfer_stops = sorted(list(transfer_stops))
    finish_stops = sorted(list(finish_stops))
    return start_stops, transfer_stops, finish_stops



def on_demand_stops_test(json_data, transfer_stops):
    wrong_stops = []
    for item in json_data:
        stop_name = item['stop_name']
        if item['stop_type'] == 'O' and stop_name in transfer_stops:
            wrong_stops.append(stop_name)
    print('On demand stops test:')
    if wrong_stops:
        print('Wrong stop type:', sorted(wrong_stops))
    else:
        print('OK')


data = json.loads(input())
dictionary = get_route_dictionary(data)
start_stops, transfer_stops, finish_stops = process_route_dictionary(dictionary)

on_demand_stops_test(data, transfer_stops)
