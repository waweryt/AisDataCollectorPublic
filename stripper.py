'''
This file reform the collected data
© waweryt and blissy
'''

import re

with open(r'paste path to file with collected txt file data here', 'r') as file:
    lines = file.readlines()

pattern = r'^\d+\||\|\d+|\| \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+$'
lenght_check = r'^![A-Za-z]{5},\d,\d{1},\d{4},[AB].*\*.*$'

processed_lines = []
for line in lines:
        processed_line = re.sub(pattern, '', line).lstrip('0123456789 |')
        if re.match(lenght_check,processed_line):
              processed_lines.append(processed_line)
with open('11.txt', 'w') as new_file:
      new_file.write('\n'.join(processed_lines))
