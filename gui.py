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
		self.PURPLE = (75,37,109)
		self.TEAL = (0,176,178)
		self.SLATE = (63,100,126)
		self.LIME = (149,212,122)


		self.graphColors = [self.RED,self.GREEN,self.BLUE,self.PURPLE,self.TEAL,self.SLATE,self.LIME]

		self.PI = 3.141592653

		self.screenWidth = 800
		self.screenHeight = 480

		self.size = (self.screenWidth, self.screenHeight)
		self.screen = pg.display.set_mode(self.size, pg.FULLSCREEN)

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

	def smallgraph(self, x, y, width, height, maxX, maxY, minY, time, data, sensorLabel):
		sLabel = self.myfont.render(sensorLabel,1,self.BLACK)
		self.screen.blit(sLabel,(2,y+height))
		i = 0
		while i < len(time) - 1:
			#scale the lines to the appropirate width and height
			x1 = self.translate(time[i],time[0],maxX+time[0],0,width)
			x2 = self.translate(time[i+1],time[0],maxX+time[0],0,width)
			
			# if there are multiple lines per sensor, draw all the lines
			j = 0 
			# print("checking data length "+str(len(data[i])))
			for gas in data[i]:
				# print(str(gas))
				# print("checking data length "+str(len(data[i][gas])))
				y1 = self.translate(round(data[i][gas]),0,maxY,0,height-self.fontsize)
				y2 = self.translate(round(data[i + 1][gas]),0,maxY,0,height-self.fontsize)
				pg.draw.line(self.screen, self.graphColors[j], (x1,y+height-y1-self.fontsize),(x2,y+height-y2-self.fontsize))
				if i == len(time) - 2:
					ppmLabel = self.myfont.render(str(round(data[i][gas])),1,self.graphColors[j])
					self.screen.blit(ppmLabel,(x2+5,y+height/2-self.fontsize/2))
				j+=1

			if i == len(time) - 2:
				pg.draw.line(self.screen, self.BLACK, (x2,y),(x2,y+height-self.fontsize),1)
				pg.draw.line(self.screen, self.BLACK, (0,y+height-self.fontsize),(x2,y+height-self.fontsize),1)
				k = 0
				while k < 5: #To Do: make this more robust
					timelabel = self.myfont.render(str(k),1,self.BLACK)
					self.screen.blit(timelabel,(x2-k*width/5-5,y+height-self.fontsize))
					k+=1
				pg.draw.line(self.screen, self.BLACK, (x2+1,y+height-y2),(x2+4,y+height-y2),1)
				

			# pg.draw.line(self.screen, self.RED , (i,round(mq2[i]['GAS_LPG'])) , (i + 1,round(mq2[i + 1]['GAS_LPG'])))
			# pg.draw.line(self.screen, self.GREEN , (i,round(mq2[i]['CARBON_MONOXIDE'])) , (i + 1,round(mq2[i + 1]['CARBON_MONOXIDE'])))
			# pg.draw.line(self.screen, self.BLUE , (i,round(mq2[i]['SMOKE'])) , (i + 1,round(mq2[i + 1]['SMOKE'])))
			i += 1


	def draw(self, time, data, maxX, maxY, minY, label):
		self.screen.fill(self.WHITE)
		smallGraphWidth = self.screenWidth*0.25
		smallGraphHeight = self.screenHeight/len(data)
		i = 0
		for sensordata, max_ppm, min_ppm, sensorLabel in zip(data, maxY, minY, label):
			self.smallgraph(0 , i*smallGraphHeight , smallGraphWidth , smallGraphHeight , maxX , max_ppm, min_ppm , time , sensordata, sensorLabel)
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

