'''
This file will decode collected AIS data
© waweryt and blissy
'''

import pyais
from pyais.exceptions import MissingMultipartMessageException, InvalidNMEAMessageException

putPath = input("Enter path to file: ")
txtFile = open(putPath, 'r')
strings = txtFile.readlines()
msgCounter = 0

newTXT = open('decoded.txt', 'w')

for line in strings:
    data = txtFile.readlines()
    msgCounter += 1
    if line.startswith('$'):
        continue
    elif line.startswith('!'):
        try:
            decoded = pyais.decode(line)
            print(f'{msgCounter}: {decoded}')
            newTXT.write('\n')
            newTXT.write(str(decoded))
        except MissingMultipartMessageException:
            print(f"{msgCounter}: {line} MissingMultipartMessageException")
        except InvalidNMEAMessageException:
            print(f"{msgCounter}: {line} InvalidNMEAMessageException")
    else:
        continue
