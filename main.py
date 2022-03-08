import serial, time
import datetime as datetime
from MQ2PPM import MQ2PPM
from MQ3PPM import MQ3PPM
from MQ4PPM import MQ4PPM
from MQ5PPM import MQ5PPM
from MQ6PPM import MQ6PPM
from MQ7PPM import MQ7PPM
from MQ8PPM import MQ8PPM
from MQ9PPM import MQ9PPM
from MQ135PPM import MQ135PPM
from gui import gui
import ast

class AirSensor:

	def __init__(self):
		self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
		self.timeStamp = []
		self.sensorArray = [MQ2PPM(),MQ3PPM(),MQ4PPM(),
						MQ5PPM(),MQ6PPM(),MQ7PPM(),
						MQ8PPM(),MQ9PPM(),MQ135PPM()]
		self.gui = gui()
		self.maxGraphTime = 90 #seconds. any data over this amount is removed
		self.seconds = 0
		self.secondsPassed = 0

	def getDataFromArduino(self):
		# to do
		if self.ser.in_waiting > 0:
			return str(self.ser.readline().decode('utf-8').rstrip())

	def parseData(self, raw):
		if raw[0] == '{': #make sure we're starting from the start of the dictionary
			result = ast.literal_eval(raw)
			return result
		return None

	def manageData(self, data):
		if self.secondsPassed > self.maxGraphTime: #remove the first index
			del self.timeStamp[0] 
			lengthOfTime = len(self.timeStamp)
			for sensor in self.sensorArray:
				if len(sensor.data) >= lengthOfTime:
					del sensor.data[0]

		try :
			for name, value in data.items():
				for sensor in self.sensorArray:
					if name == sensor.LABEL:
						if sensor.isCalibrationDone == False:
							sensor.MQCalibration(value)
						else:
							sensor.data.append(sensor.getMQPPM(value))
						if name=='MQ2':
							self.timeStamp.append(time.time()-self.seconds)
		except:
			print("Issue reading arduino serial data.")
		
	def __call__(self):
		
		self.ser.reset_input_buffer()
		time.sleep(1)
		quit = False
		self.seconds = time.time() #when we started the program

		# try:
		while quit == False:
			if self.ser.isOpen():
				raw = self.getDataFromArduino()
				if raw is not None:
					# print(raw)
					data = self.parseData(raw)
					if data is not None and len(data)>0 and len(data)<10:
						self.manageData(data)
						quit = self.gui.draw(
							self.timeStamp, 
							self.sensorArray,
							self.maxGraphTime)
						self.secondsPassed = (self.timeStamp[len(self.timeStamp)-1] - self.timeStamp[0])
		# except:
		# 	print("Exiting")

a = AirSensor()
a()