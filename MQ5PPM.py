import time
import math
from MQFunctions import MQFunctions

class MQ5PPM(MQFunctions):

    RL_VALUE                     = 20        # define the load resistance on the board, in kilo ohms
    RO_CLEAN_AIR_FACTOR          = 6.5     # RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                            # which is derived from the chart in datasheet
    MIN_PPM = 200 #unclear if this is accurate. got it from data sheet.
    MAX_PPM = 10000
    LABEL = "MQ5"

    def __init__(self):
        self.sensorNumber = 5
        
        # following values are derived from the logarithmic graphs 
        # from the datasheets format: [x, y, slope], then we can use y=mx+b to figure out
        # then in another equation below we will use these values to determine the ppm
        # self.LPGCurve = [2.3,0.21,-0.47]    
        # self.MethaneCurve = [2.3,0.72,-0.34]     
        self.gases = {"LPG":[2.3,0.21,-0.47],
                    "C6H6":[2.3,0.72,-0.34]}
        super(MQ5PPM, self).__init__(self.gases)