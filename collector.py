'''
This file collects AIS data

© waweryt and blissy
'''

import os
import serial
import datetime
import sqlite3 as sl

signalId = 0
currentDate = datetime.datetime.now()
print(f"-------{currentDate.strftime('%Y-%m-%d_%H-%M-%S')}-------")

if os.path.exists(r'txtFiles') and os.path.exists(r'dbFiles'):
	fileNameTxt = f"signalData_{currentDate.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
	txtFile = open(f"txtFiles/{fileNameTxt}", 'w')
	fileNameDB = f"signalData_{currentDate.strftime('%Y-%m-%d_%H-%M-%S')}.db"
	dbFile = open(f"dbFiles/{fileNameDB}", 'w')

	txtContent = os.listdir('txtFiles')
	dbContent = os.listdir('dbFiles')
	print(f"Found txt directory, contains: {txtContent} \nFound db directory, contains: {dbContent}")
	
	dbFilePath = os.path.join('dbFiles', dbContent[-1])
	conn = sl.connect(dbFilePath)
	cursor = conn.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS ReceivedData(id INTEGER PRIMARY KEY AUTOINCREMENT,
	data TEXT, currentDate TIMESTAMP)''')
	txtFile.write(f"----------- Start receiving {currentDate}-----------")
	input("Убедитесь, что передатчик подключен к компьютеру и нажмите Enter")

	ser = serial.Serial('COM1', 38400, timeout=0, parity=serial.PARITY_NONE, rtscts=1)
	while True:
		while ser.inWaiting():
			signalId += 1
			data = ser.readline().decode().strip()
			txtFile.write(f"{signalId} | {data} | {currentDate}")
			
			cursor.execute('''INSERT INTO ReceivedData(data,currentDate) VALUES (?,?)''', (data, currentDate))
			conn.commit()
			print("Written to database")
			print(data)
			print(currentDate)
			print('-------------------')

else:
	os.makedirs('dbFiles')
	os.makedirs('txtFiles')
	print("Directories created, open me again")
	print("Better call @waweryt!")
