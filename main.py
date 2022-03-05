import serial
import re

class AirSensor:

	def __init__(self):
		self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

	def getDataFromArduino(self):
		# to do
		if self.ser.in_waiting > 0:
			return self.ser.readline().decode('utf-8').rstrip()

	def parseData(self, raw):
		# to do
		result = re.search(":(.*)-",raw)
		return result

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
				print(data.len())
			# saveData(data)
			# visualizeData(data)

a = AirSensor()
a()