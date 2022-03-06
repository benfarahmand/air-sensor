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

class AirSensor:

	def __init__(self):
		self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
		self.timeStamp = []
		self.mq2 = [] 
		self.mq3 = [] 
		self.mq4 = [] 
		self.mq5 = [] 
		self.mq6 = [] 
		self.mq7 = [] 
		self.mq8 = [] 
		self.mq9 = [] 
		self.mq135 = [] 
		self.mq2ppm = MQ2PPM()
		self.mq3ppm = MQ3PPM()
		self.mq4ppm = MQ4PPM()
		self.mq5ppm = MQ5PPM()
		self.mq6ppm = MQ6PPM()
		self.mq7ppm = MQ7PPM()
		self.mq8ppm = MQ8PPM()
		self.mq9ppm = MQ9PPM()
		self.mq135ppm = MQ135PPM()
		self.gui = gui()

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
				# print("TIME: "+str(datetime.datetime.now().time()))
				# print("MQ2:"+str(self.mq2ppm.getMQPPM(value)))
				self.mq2.append(self.mq2ppm.getMQPPM(value))
			# if index == 3:
			# 	print("MQ3:"+str(self.mq3ppm.getMQPPM(value)))
			# 	# self.mq3.append(value)
			# if index == 4:
			# 	print("MQ4:"+str(self.mq4ppm.getMQPPM(value)))
			# 	# self.mq4.append(value)
			# if index == 5:
			# 	print("MQ5:"+str(self.mq5ppm.getMQPPM(value)))
			# 	# self.mq5.append(value)
			# if index == 6:
			# 	print("MQ6:"+str(self.mq6ppm.getMQPPM(value)))
			# 	# self.mq6.append(value)
			# if index == 7:
			# 	print("MQ7:"+str(self.mq7ppm.getMQPPM(value)))
			# 	# self.mq7.append(value)
			# if index == 8:
			# 	print("MQ8:"+str(self.mq8ppm.getMQPPM(value)))
			# 	# self.mq8.append(value)
			# if index == 9:
			# 	print("MQ9:"+str(self.mq9ppm.getMQPPM(value)))
			# 	# self.mq9.append(value)
			# if index == 135:
			# 	print("MQ135:"+str(self.mq135ppm.getMQPPM(value)))
				# self.mq135.append(value)
		except:
			print("An exception occurred")

	def __call__(self):
		
		self.ser.reset_input_buffer()
		time.sleep(2)
		quit = False
		# try:
		while quit == False:
			if self.ser.isOpen():
				raw = self.getDataFromArduino()
				if raw is not None:
					# print(raw)
					data = self.parseData(raw)
					if data is not None and len(data)>0 and len(data)<10:
						self.storeDataInArray(data)
						if len(self.timeStamp) > 3:
							quit = self.gui.draw(self.timeStamp, self.mq2)
		# except:
		# 	print("Exiting")

a = AirSensor()
a()