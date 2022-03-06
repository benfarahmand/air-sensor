import pygame as pg

class gui:

	def __init__(self):
		self.pg.init()
		self.myfont = pg.font.SysFont("monospace", 15)

		
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
		self.screen = self.pg.display.set_mode(self.size, self.pg.FULLSCREEN)

		# Used to manage how fast the screen updates
		self.clock = self.pg.time.Clock()

	def draw(self, time, mq2):
		self.screen.fill(self.WHITE)
		i = 0 
		while i < len(time) - 1:
			self.pg.draw.line(self.screen, self.RED , (i,round(mq2[i]['GAS_LPG'])) , (i + 1,round(mq2[i + 1]['GAS_LPG'])))
			self.pg.draw.line(self.screen, self.GREEN , (i,round(mq2[i]['CARBON_MONOXIDE'])) , (i + 1,round(mq2[i + 1]['CARBON_MONOXIDE'])))
			self.pg.draw.line(self.screen, self.BLUE , (i,round(mq2[i]['SMOKE'])) , (i + 1,round(mq2[i + 1]['SMOKE'])))
			i += 1

		self.pg.display.flip()

		for event in self.pg.event.get():
			if event.type == self.pg.MOUSEBUTTONDOWN:
				print("Mouse Event Detected")
				return True

		return False

# def clickEvent():

