from gui import gui
import datetime as datetime
import time
from random import randrange

class guitest:
	def __init__(self):
		self.g = gui()
		self.randomData = []
		self.timeStamp = []
		self.numberOfGraphs = 3
		self.maxGraphTime = 300 #seconds. any data over this amount is removed
		self.seconds = 0
		self.secondsPassed = 0
		self.maxPPM = 1000

	def __call__(self):
		quit = False
		self.seconds = time.time() #when we started the program
		while quit == False:
			if self.secondsPassed > self.maxGraphTime: #remove the first index
				del self.randomData[0] 
				del self.timeStamp[0]
				# self.seconds = time.time() #update this time
			self.randomData.append({"GAS":randrange(1000),"H2":randrange(1000),"NH3":randrange(1000)})
			# self.timeStamp.append(datetime.datetime.now())
			self.timeStamp.append(time.time()-self.seconds)
			time.sleep(.1)
			if len(self.timeStamp) > 3:
				quit = self.g.draw(self.timeStamp,self.randomData, self.numberOfGraphs, self.maxGraphTime, self.maxPPM)
				self.secondsPassed = (self.timeStamp[len(self.timeStamp)-1] - self.timeStamp[0])
				

test = guitest()
test()