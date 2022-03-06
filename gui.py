import pygame as pg

class gui:

	def __init__(self):
		pg.init()
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
		self.screen = pg.display.set_mode(self.size, pg.FULLSCREEN)

		# Used to manage how fast the screen updates
		self.clock = pg.time.Clock()

	def draw(self, time, mq2):
		self.screen.fill(self.WHITE)
		i = 0 
		while i < len(time) - 1:
			pg.draw.line(screen, self.BLACK,(i,mq2[i]['GAS_LPG']),(i + 1,mq2[i + 1]['GAS_LPG'])
			i = i + 1

		pg.display.flip()

		for event in self.pg.event.get():
			if event.type == self.pg.MOUSEBUTTONDOWN:
				return True

		return False

# def clickEvent():

