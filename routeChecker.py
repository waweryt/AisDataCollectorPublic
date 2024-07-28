'''
This file to search in decoded file concrete ship by his MMSI
@ waweryt and blissy
'''

import re

search_mmsi = 'put there mmsi'
pattern = r'mmsi=' + search_mmsi

with open('decoded.txt') as f:
    for line in f:
        if re.search(pattern, line):
            match = re.search(r'speed=(\d+\.\d+)', line)
            speed = match.group(1) if match else None

            match = re.search(r'lon=(-?\d+\.\d+)', line)
            lon = match.group(1) if match else None

            match = re.search(r'lat=(-?\d+\.\d+)', line)
            lat = match.group(1) if match else None

            match = re.search(r'course=(\d+\.\d+)', line)
            course = match.group(1) if match else None

            print(f"{search_mmsi}, {speed}, {lon}, {lat}, {course}")
