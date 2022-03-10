import time
import math
from MQFunctions import MQFunctions

class MQ8PPM(MQFunctions):
    #v1
    RL_VALUE                     = 10
    RO_CLEAN_AIR_FACTOR          = 70

    #v2
    # RL_VALUE                     = 4.7        # define the load resistance on the board, in kilo ohms
    # RO_CLEAN_AIR_FACTOR          = 1        # RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                             # which is derived from the chart in datasheet
    MIN_PPM = 100 #unclear if this is accurate. got it from data sheet.
    MAX_PPM = 10000
    LABEL = "MQ8"

    def __init__(self):
        self.sensorNumber = 8
        
        # following values are derived from the logarithmic graphs 
        # from the datasheets format: [x, y, slope], then we can use y=mx+b to figure out
        # then in another equation below we will use these values to determine the ppm
        
        #something is off with these numbers from the datasheet
        #found a different data sheet for mq8 with a different curve, trying that instead
        # self.H2Curve = [2.3,0.93,-1.44] #v1
        # self.H2Curve = [2.0,-0.6,-0.4]#data sheet from sparkfun

        self.gases = {"H2":[2.3,0.93,-1.44],
                    "LPG":[2.30,1.54,-0.24],
                    "CH4":[2.30,1.72,-0.15],
                    "CO":[2.30,1.81,-0.12],
                    "ALCOHOL":[2.30,1.18,-0.47]}
        super(MQ8PPM, self).__init__(self.gases)