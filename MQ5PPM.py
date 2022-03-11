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
        self.gases = {"LPG":[2.30,-0.15,-0.67],
                    "CH$":[2.30,-0.02,-0.58],
                    "H2":[2.30,0.26,-0.25],
                    "ALCOHOL":[2.30,0.54,-0.21],
                    "CO":[2.30,0.60,-0.14]}
        super(MQ5PPM, self).__init__(self.gases)