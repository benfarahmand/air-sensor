import serial, time
import datetime as datetime

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

	def getDataFromArduino(self):
		# to do
		if self.ser.in_waiting > 0:
			return str(self.ser.readline().decode('utf-8').rstrip())

	def parseData(self, raw):
		# to do
		result = raw[raw.find("Q")+1 : raw.find(" -")]
		return result

	def storeDataInArray(self, data):
		print("store")
		# self.timeStamp.append(datetime.datetime.now().time())
		# self.mq2.append()
		# self.mq3.append()
		# self.mq4.append()
		# self.mq5.append()
		# self.mq6.append()
		# self.mq7.append()
		# self.mq8.append()
		# self.mq9.append()
		# self.mq135.append()

	# def saveData(data):
		# to do

	# def visualizeData(data):
		# to do

	def __call__(self):
		
		self.ser.reset_input_buffer()
		time.sleep(2)
		while True:
			if self.ser.isOpen():
				raw = self.getDataFromArduino()
				if raw is not None:
					# print(raw)
					data = self.parseData(raw)
					if data is not None and len(data)>0 and len(data)<10:
						print(data)
						self.storeDataInArray(data)
				# saveData(data)
				# visualizeData(data)

a = AirSensor()
a()