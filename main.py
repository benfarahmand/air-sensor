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
		# self.mq2 = [] 
		# self.mq3 = [] 
		# self.mq4 = [] 
		# self.mq5 = [] 
		# self.mq6 = [] 
		# self.mq7 = [] 
		# self.mq8 = [] 
		# self.mq9 = [] 
		# self.mq135 = [] 
		self.sensorArray = [MQ2PPM(),MQ3PPM(),MQ4PPM(),
						MQ5PPM(),MQ6PPM(),MQ7PPM(),
						MQ8PPM(),MQ9PPM(),MQ135PPM()]
		# self.mq2ppm = MQ2PPM()
		# self.mq3ppm = MQ3PPM()
		# self.mq4ppm = MQ4PPM()
		# self.mq5ppm = MQ5PPM()
		# self.mq6ppm = MQ6PPM()
		# self.mq7ppm = MQ7PPM()
		# self.mq8ppm = MQ8PPM()
		# self.mq9ppm = MQ9PPM()
		# self.mq135ppm = MQ135PPM()
		self.gui = gui()
		self.maxGraphTime = 90 #seconds. any data over this amount is removed
		self.seconds = 0
		self.secondsPassed = 0

	def getDataFromArduino(self):
		# to do
		if self.ser.in_waiting > 0:
			return str(self.ser.readline().decode('utf-8').rstrip())

	def parseData(self, raw):
		# to do
		result = raw[raw.find("Q")+1 : raw.find(" -")]
		return result

	def manageData(self, data):
		if self.secondsPassed > self.maxGraphTime: #remove the first index
			del self.timeStamp[0] 
			lengthOfTime = len(self.timeStamp)
			for sensor in self.sensorArray:
				if len(sensor.data) >= lengthOfTime:
					del sensor.data[0]
			# if len(self.mq2) >= lengthOfTime:
			# 	del self.mq2[0]
			# if len(self.mq3) >= lengthOfTime:
			# 	del self.mq3[0]
			# if len(self.mq4) >= lengthOfTime:
			# 	del self.mq4[0]
			# if len(self.mq5) >= lengthOfTime:
			# 	del self.mq5[0]
			# if len(self.mq6) >= lengthOfTime:
			# 	del self.mq6[0]
			# if len(self.mq7) >= lengthOfTime:
			# 	del self.mq7[0]
			# if len(self.mq8) >= lengthOfTime:
			# 	del self.mq8[0]
			# if len(self.mq9) >= lengthOfTime:
			# 	del self.mq9[0]
			# if len(self.mq135) >= lengthOfTime:
			# 	del self.mq135[0]

		try :
			index = int(data[0 : data.find(":")])
			value = int(data[data.find(":")+2 : len(data)])
		except:
			print("Issue reading arduino serial data.")
		for sensor in self.sensorArray:
			if index == sensor.sensorNumber:
				if sensor.isCalibrationDone == False:
					sensor.MQCalibration(value)
				else:
					sensor.data.append(sensor.getMQPPM(value))
				if sensor.sensorNumber==2:
					self.timeStamp.append(time.time()-self.seconds)
# 
		# if index == 2:
		# 	if self.mq2ppm.isCalibrationDone == False:
		# 		self.mq2ppm.MQCalibration(value)
		# 	else:
		# 		self.mq2.append(self.mq2ppm.getMQPPM(value))
		# 	# print(str(value)+" : "+str(self.mq2[len(self.mq2)-1]))
		# if index == 3:
		# 	# print("MQ3:"+str(self.mq3ppm.getMQPPM(value)))
		# 	if self.mq2ppm.isCalibrationDone == False:
		# 		self.mq2ppm.MQCalibration(value)
		# 	else:
		# 		self.mq2.append(self.mq2ppm.getMQPPM(value))
		# 	# print(str(value)+" : "+str(self.mq2[len(self.mq2)-1]))
		# 	# print(str(value)+" : "+str(self.mq3[len(self.mq3)-1]))
		# if index == 4:
		# 	# print("MQ4:"+str(self.mq4ppm.getMQPPM(value)))
		# 	if self.mq2ppm.isCalibrationDone == False:
		# 		self.mq2ppm.MQCalibration(value)
		# 	else:
		# 		self.mq2.append(self.mq2ppm.getMQPPM(value))
		# if index == 5:
		# 	# print("MQ5:"+str(self.mq5ppm.getMQPPM(value)))
		# 	if self.mq2ppm.isCalibrationDone == False:
		# 		self.mq2ppm.MQCalibration(value)
		# 	else:
		# 		self.mq2.append(self.mq2ppm.getMQPPM(value))
		# if index == 6:
		# 	# print("MQ6:"+str(self.mq6ppm.getMQPPM(value)))
		# 	if self.mq2ppm.isCalibrationDone == False:
		# 		self.mq2ppm.MQCalibration(value)
		# 	else:
		# 		self.mq2.append(self.mq2ppm.getMQPPM(value))
		# if index == 7:
		# 	# print("MQ7:"+str(self.mq7ppm.getMQPPM(value)))
		# 	if self.mq2ppm.isCalibrationDone == False:
		# 		self.mq2ppm.MQCalibration(value)
		# 	else:
		# 		self.mq2.append(self.mq2ppm.getMQPPM(value))
		# if index == 8:
		# 	# print("MQ8:"+str(self.mq8ppm.getMQPPM(value)))
		# 	if self.mq2ppm.isCalibrationDone == False:
		# 		self.mq2ppm.MQCalibration(value)
		# 	else:
		# 		self.mq2.append(self.mq2ppm.getMQPPM(value))
		# if index == 9:
		# 	# print("MQ9:"+str(self.mq9ppm.getMQPPM(value)))
		# 	if self.mq2ppm.isCalibrationDone == False:
		# 		self.mq2ppm.MQCalibration(value)
		# 	else:
		# 		self.mq2.append(self.mq2ppm.getMQPPM(value))
		# if index == 135:
		# 	# print("MQ135:"+str(self.mq135ppm.getMQPPM(value)))
		# 	if self.mq2ppm.isCalibrationDone == False:
		# 		self.mq2ppm.MQCalibration(value)
		# 	else:
		# 		self.mq2.append(self.mq2ppm.getMQPPM(value))

	# def calibrateSensors(self, data):
	# 	try :
	# 		index = int(data[0 : data.find(":")])
	# 		value = int(data[data.find(":")+2 : len(data)])
	# 	except:
	# 		print("Issue reading arduino serial data.")
	# 	if index == 2 and self.mq2ppm.isCalibrationDone == False:
	# 		self.mq2ppm.MQCalibration(value)
	# 	if index == 3 and self.mq3ppm.isCalibrationDone == False:
	# 		self.mq3ppm.MQCalibration(value)
	# 	if index == 4 and self.mq4ppm.isCalibrationDone == False:
	# 		self.mq4ppm.MQCalibration(value)
	# 	if index == 5 and self.mq5ppm.isCalibrationDone == False:
	# 		self.mq5ppm.MQCalibration(value)
	# 	if index == 6 and self.mq6ppm.isCalibrationDone == False:
	# 		self.mq6ppm.MQCalibration(value)
	# 	if index == 7 and self.mq7ppm.isCalibrationDone == False:
	# 		self.mq7ppm.MQCalibration(value)
	# 	if index == 8 and self.mq8ppm.isCalibrationDone == False:
	# 		self.mq8ppm.MQCalibration(value)
	# 	if index == 9 and self.mq9ppm.isCalibrationDone == False:
	# 		self.mq9ppm.MQCalibration(value)
	# 	if index == 135 and self.mq135ppm.isCalibrationDone == False:
	# 		self.mq135ppm.MQCalibration(value)

		
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
						# if (self.mq2ppm.isCalibrationDone == True and 
						# 	self.mq3ppm.isCalibrationDone == True and 
						# 	self.mq4ppm.isCalibrationDone == True and 
						# 	self.mq5ppm.isCalibrationDone == True and 
						# 	self.mq6ppm.isCalibrationDone == True and 
						# 	self.mq7ppm.isCalibrationDone == True and 
						# 	self.mq8ppm.isCalibrationDone == True and 
						# 	self.mq9ppm.isCalibrationDone == True and 
						# 	self.mq135ppm.isCalibrationDone == True):
						self.storeDataInArray(data)
							# l = 4
							# if (len(self.timeStamp) > l and 
							# 	len(self.mq2) > l and len(self.mq3) > l and len(self.mq4) > l and
							# 	len(self.mq5) > l and len(self.mq6) > l and len(self.mq7) > l and
							# 	len(self.mq8) > l and len(self.mq9) > l and len(self.mq135) > l):
						quit = self.gui.draw(
							self.timeStamp, 
							self.sensorArray,
							self.maxGraphTime)
								# [self.mq2,self.mq3,self.mq4,
								# self.mq5,self.mq6,self.mq7,
								# self.mq8,self.mq9,self.mq135],
								# self.maxGraphTime,
								# [self.mq2ppm,self.mq3ppm,self.mq4ppm,
								# self.mq5ppm,self.mq6ppm,self.mq7ppm,
								# self.mq8ppm,self.mq9ppm,self.mq135ppm])
						self.secondsPassed = (self.timeStamp[len(self.timeStamp)-1] - self.timeStamp[0])
						# else:
						# 	self.calibrateSensors(data)
		# except:
		# 	print("Exiting")

a = AirSensor()
a()