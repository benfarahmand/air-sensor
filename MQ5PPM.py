import time
import math
from MQFunctions import MQFunctions

class MQ5PPM(MQFunctions):

    RL_VALUE                     = 20 
    RO_CLEAN_AIR_FACTOR          = 6.5
    MIN_PPM = 200
    MAX_PPM = 10000
    LABEL = "MQ5"

    def __init__(self):
        self.sensorNumber = 5
        
        #format for array: [x, y, slope, min_Rs/Ro, max_Rs/Ro]    
        self.gases = {
                    "CH4":[2.30,-0.02,-0.58,0.1,0.95],
                    "LPG":[2.30,-0.15,-0.67,0.05,0.7],
                    "H2":[2.30,0.26,-0.25,0.68,1.8],
                    "ALCOHOL":[2.30,0.54,-0.21,1.55,3.5],
                    "CO":[2.30,0.60,-0.14,2.35,4]
                    }
        super(MQ5PPM, self).__init__(self.gases)