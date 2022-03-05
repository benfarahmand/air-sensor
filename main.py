import serial
# import re

class AirSensor:

	def __init__(self):
		self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
		self.mq2 = [] # LPG, Propane and Hydrogen
		self.mq3 = [] # Alcohol, Ethanol
		self.mq4 = [] # Methane, Natural Gas
		self.mq5 = [] # LPG, Natural Gas
		self.mq6 = [] # LPG, Iso-butane, Propane
		self.mq7 = [] # Carbon Monoxide
		self.mq8 = [] # Hydrogen
		self.mq9 = [] # Methan, Propane, and CO
		self.mq135 = [] # NH3, NOx, Alcohol, Benzene, Smoke, CO2

	def getDataFromArduino(self):
		# to do
		if self.ser.in_waiting > 0:
			return self.ser.readline().decode('utf-8').rstrip()

	def parseData(self, raw):
		# to do
		result = raw[raw.find(": ")+1 : raw.find(" -")]
		return result

	def storeDataInArray(self, data):
		self.mq2 = [] # LPG, Propane and Hydrogen
		self.mq3 = [] # Alcohol, Ethanol
		self.mq4 = [] # Methane, Natural Gas
		self.mq5 = [] # LPG, Natural Gas
		self.mq6 = [] # LPG, Iso-butane, Propane
		self.mq7 = [] # Carbon Monoxide
		self.mq8 = [] # Hydrogen
		self.mq9 = [] # Methan, Propane, and CO
		self.mq135 = [] # NH3, NOx, Alcohol, Benzene, Smoke, CO2

	# def saveData(data):
		# to do

	# def visualizeData(data):
		# to do

	def __call__(self):
		
		self.ser.reset_input_buffer()
		while True:
			raw = self.getDataFromArduino()
			if raw is not None:
				# print(raw)
				data = self.parseData(raw)
				if data is not None:
					print(data[0])
					# storeDataInArray(data)
			# saveData(data)
			# visualizeData(data)

a = AirSensor()
a()