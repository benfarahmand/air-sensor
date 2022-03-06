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

class AirSensor:

	def __init__(self):
		self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
		self.timeStamp = []
		self.mq2 = [] # LPG, Propane and Hydrogen
		self.mq3 = [] # Alcohol, Ethanol
		self.mq4 = [] # Methane, Natural Gas
		self.mq5 = [] # LPG, Natural Gas
		self.mq6 = [] # LPG, Iso-butane, Propane
		self.mq7 = [] # Carbon Monoxide
		self.mq8 = [] # Hydrogen
		self.mq9 = [] # Methan, Propane, and CO
		self.mq135 = [] # NH3, NOx, Alcohol, Benzene, Smoke, CO2
		self.mq2ppm = MQ2PPM()
		self.mq3ppm = MQ3PPM()
		self.mq4ppm = MQ4PPM()
		self.mq5ppm = MQ5PPM()
		self.mq6ppm = MQ6PPM()
		self.mq7ppm = MQ7PPM()
		self.mq8ppm = MQ8PPM()
		self.mq9ppm = MQ9PPM()
		self.mq135ppm = MQ135PPM()

	def getDataFromArduino(self):
		# to do
		if self.ser.in_waiting > 0:
			return str(self.ser.readline().decode('utf-8').rstrip())

	def parseData(self, raw):
		# to do
		result = raw[raw.find("Q")+1 : raw.find(" -")]
		return result

	def storeDataInArray(self, data):
		try:
			index = int(data[0 : data.find(":")])
			value = int(data[data.find(":")+2 : len(data)])
			if index == 2:
				self.timeStamp.append(datetime.datetime.now().time())
				print("TIME: "+datetime.datetime.now().time())
				print("MQ2:"+self.mq2ppm.getMQPPM(value))
				# self.mq2.append(value)
			if index == 3:
				print("MQ3:"+self.mq3ppm.getMQPPM(value))
				# self.mq3.append(value)
			if index == 4:
				print("MQ4:"+self.mq4ppm.getMQPPM(value))
				# self.mq4.append(value)
			if index == 5:
				print("MQ5:"+self.mq5ppm.getMQPPM(value))
				# self.mq5.append(value)
			if index == 6:
				print("MQ6:"+self.mq6ppm.getMQPPM(value))
				# self.mq6.append(value)
			if index == 7:
				print("MQ7:"+self.mq7ppm.getMQPPM(value))
				# self.mq7.append(value)
			if index == 8:
				print("MQ8:"+self.mq8ppm.getMQPPM(value))
				# self.mq8.append(value)
			if index == 9:
				print("MQ9:"+self.mq9ppm.getMQPPM(value))
				# self.mq9.append(value)
			if index == 135:
				print("MQ135:"+self.mq135ppm.getMQPPM(value))
				# self.mq135.append(value)
		except:
			print("An exception occurred")
		
	# def convertVoltageToPPM(self, data):
		# to do

	# def saveData(data):
		# to do

	# def visualizeData(data):
		# to do

	def __call__(self):
		
		self.ser.reset_input_buffer()
		time.sleep(2)
		# try:
		while True:
			if self.ser.isOpen():
				raw = self.getDataFromArduino()
				if raw is not None:
					# print(raw)
					data = self.parseData(raw)
					if data is not None and len(data)>0 and len(data)<10:
						self.storeDataInArray(data)
					# saveData(data)
					# visualizeData(data)
		# except:
		# 	print("Exiting")

a = AirSensor()
a()