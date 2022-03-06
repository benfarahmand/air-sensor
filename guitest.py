from gui import gui
import datetime as datetime
from random import randrange

g = gui()
randomData = []
timeStamp = []

quit = False
while quit == False:
	randomData.append(randrange(100))
	timeStamp.append(datetime.datetime.now().time())
	if len(timeStamp) > 3:
		quit = gui.draw()