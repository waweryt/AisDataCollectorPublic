"""
This file was created to search for ships in a square of coordinates
@ waweryt and blissy
"""
import re

lon_min = put there minimum value of longitude
lon_max = put there maximum value of longitude

seen_mmsi = set()

with open('put here path to decoded file') as f:
    for line in f:
        line = line.strip()

        m = re.search(r'mmsi=(\d+)', line)
        if m:
            mmsi = m.group(1)

            if mmsi not in seen_mmsi:

                speed_match = re.search(r'speed=(\d+\.\d+)', line)
                lon_match = re.search(r'lon=(\d+\.\d+)', line)
                lat_match = re.search(r'lat=(\d+\.\d+)', line)
                course_match = re.search(r'course=(\d+\.\d+)', line)

                if lon_match:
                    lon = float(lon_match.group(1))
                    if lon >= lon_min and lon <= lon_max:
                        speed = speed_match.group(1) if speed_match else None
                        lon = lon_match.group(1)
                        lat = lat_match.group(1) if lat_match else None
                        course = course_match.group(1) if course_match else None

                        print(f"{mmsi} {speed} {lon} {lat} {course}")
                        seen_mmsi.add(mmsi)
