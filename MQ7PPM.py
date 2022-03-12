import time
import math
from MQFunctions import MQFunctions

class MQ7PPM(MQFunctions):

    RL_VALUE                     = 10        
    RO_CLEAN_AIR_FACTOR          = 27        
    MIN_PPM = 20 
    MAX_PPM = 2000
    LABEL = "MQ7"

    def __init__(self):
        self.sensorNumber = 7
        
        #format for array: [x, y, slope, min_Rs/Ro, max_Rs/Ro]    
        self.gases = {"CO":[1.7,0.2,-0.66,0.09,1.6],
                    "H2":[1.7,0.15,-0.76,0.05,1.4],
                    "LPG":[1.70,0.95,-0.13,5,9],
                    "CH4":[1.70,1.02,-0.04,9,10.5],
                    "ALCOHOL":[1.70,1.03,-0.01,10.3,10.7]}
        super(MQ7PPM, self).__init__(self.gases)