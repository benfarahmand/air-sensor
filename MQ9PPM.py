import time
import math
from MQFunctions import MQFunctions

class MQ9PPM(MQFunctions):


    RL_VALUE                     = 10        # define the load resistance on the board, in kilo ohms
    RO_CLEAN_AIR_FACTOR          = 10        # RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                             # which is derived from the chart in datasheet
    MIN_PPM = 500 #unclear if this is accurate. got it from data sheet.
    MAX_PPM = 10000
    LABEL = "MQ9"

    def __init__(self):
        self.sensorNumber = 9
        
        # following values are derived from the logarithmic graphs 
        # from the datasheets format: [x, y, slope], then we can use y=mx+b to figure out
        # then in another equation below we will use these values to determine the ppm
        # self.LPGCurve = [2.3,0.3,-0.46]    
        # self.COCurve = [2.3,0.2,-0.43]
        # self.MethaneCurve = [2.3,0.48,-0.37]
        self.gases = {"LPG":[2.3,0.3,-0.46],
                    "CO":[2.3,0.2,-0.43],
                    "CH4":[2.3,0.48,-0.37]}
        super(MQ9PPM, self).__init__(self.gases)