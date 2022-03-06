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
		# while i < len(time)
		# 	pg.draw.line(screen, self.BLACK,(time[i],mq2[i]['GAS_LPG']),(screenWidth*0.9,screenHeight*0.9))

		pg.display.flip()

# def clickEvent():

