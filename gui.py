import pygame as pg

class gui:

	def __init__(self):
		pg.init()
		self.fontsize = 15
		self.myfont = pg.font.SysFont("monospace", self.fontsize)

		
		#define some colors
		self.BLACK = (0,0,0)
		self.WHITE = (255,255,255)
		self.BLUE = (0, 0, 255)
		self.GREEN = (0, 255, 0)
		self.RED = (255, 0, 0)

		self.PI = 3.141592653

		self.screenWidth = 800
		self.screenHeight = 480

		self.size = (self.screenWidth, self.screenHeight)
		self.screen = pg.display.set_mode(self.size)#, pg.FULLSCREEN)

		# Used to manage how fast the screen updates
		self.clock = pg.time.Clock()

	def translate(self,value, leftMin, leftMax, rightMin, rightMax):
		# Figure out how 'wide' each range is
		leftSpan = leftMax - leftMin
		rightSpan = rightMax - rightMin

		# Convert the left range into a 0-1 range (float)
		valueScaled = float(value - leftMin) / float(leftSpan)

		# Convert the 0-1 range into a value in the right range.
		return rightMin + (valueScaled * rightSpan)

	def smallgraph(self, x, y, width, height, maxX, maxY, time, data):
		i = 0
		while i < len(time) - 1:
			#scale the lines to the appropirate width and height
			x1 = self.translate(time[i],time[0],maxX+time[0],0,width)
			y1 = self.translate(round(data[i]),0,maxY,0,height)
			x2 = self.translate(time[i+1],time[0],maxX+time[0],0,width)
			y2 = self.translate(round(data[i + 1]),0,maxY,0,height)
			
			pg.draw.line(self.screen, self.BLACK, (x1,y+height-y1),(x2,y+height-y2))
			if i == len(time) - 2:
				pg.draw.line(self.screen, self.BLACK, (x2,y+2),(x2,y+height-2),1)
				pg.draw.line(self.screen, self.BLACK, (x2+1,y+height-y2),(x2+4,y+height-y2),1)
				label = self.myfont.render(str(round(data[i + 1])),1,self.BLACK)
				self.screen.blit(label,(x2+5,y+height/2-self.fontsize/2))
			# pg.draw.line(self.screen, self.RED , (i,round(mq2[i]['GAS_LPG'])) , (i + 1,round(mq2[i + 1]['GAS_LPG'])))
			# pg.draw.line(self.screen, self.GREEN , (i,round(mq2[i]['CARBON_MONOXIDE'])) , (i + 1,round(mq2[i + 1]['CARBON_MONOXIDE'])))
			# pg.draw.line(self.screen, self.BLUE , (i,round(mq2[i]['SMOKE'])) , (i + 1,round(mq2[i + 1]['SMOKE'])))
			i += 1


	def draw(self, time, data, numberOfGraphs, maxX, maxY):
		self.screen.fill(self.WHITE)
		smallGraphWidth = self.screenWidth*0.25
		smallGraphHeight = self.screenHeight/numberOfGraphs
		i = 0
		while i < numberOfGraphs:
			self.smallgraph(0 , i*smallGraphHeight , smallGraphWidth , smallGraphHeight , maxX , maxY , time , data)
			i += 1
		

		pg.display.flip()

		for event in pg.event.get():
			if event.type == pg.MOUSEBUTTONDOWN:
				# To Do: handle touch events for each graph
				# clicking on a graph should bring it to the forefront and make it bigger, so we can do closer inspection
				print("Mouse Event Detected")
				return True

		return False

# def clickEvent():

