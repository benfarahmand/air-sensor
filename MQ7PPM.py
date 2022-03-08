import time
import math
from MQFunctions import MQFunctions

class MQ7PPM(MQFunctions):

    RL_VALUE                     = 10        # define the load resistance on the board, in kilo ohms
    RO_CLEAN_AIR_FACTOR          = 27        # RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                             # which is derived from the chart in datasheet
    MIN_PPM = 20 #unclear if this is accurate. got it from data sheet.
    MAX_PPM = 2000
    LABEL = "MQ7"

    def __init__(self):
        self.sensorNumber = 7
        
        # following values are derived from the logarithmic graphs 
        # from the datasheets format: [x, y, slope], then we can use y=mx+b to figure out
        # then in another equation below we will use these values to determine the ppm
        # self.COCurve = [1.7,0.2,-0.66]    
        # self.H2Curve = [1.7,0.15,-0.76]     

        self.gases = {"CO":[1.7,0.2,-0.66],
                    "H2":[1.7,0.15,-0.76]}
        super(MQ7PPM, self).__init__(self.gases)