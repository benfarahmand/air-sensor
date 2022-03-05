import serial
import re

class AirSensor:
	
	def getDataFromArduino(ser):
		# to do
		if ser.in_waiting > 0:
			return ser.readline().decode('utf-8').rstrip()

	def parseData(raw):
		# to do
		result = re.search(":(.*)-",raw)
		return result

	# def saveData(data):
		# to do

	# def visualizeData(data):
		# to do

	def main():
		ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
		ser.reset_input_buffer()
		while True:
			raw = getDataFromArduino(ser)
			data = parseData(raw)
			print(data)
			# saveData(data)
			# visualizeData(data)

a = main()
a()