import time
import math
from MQFunctions import MQFunctions

class MQ6PPM(MQFunctions):
    RL_VALUE                     = 20        
    RO_CLEAN_AIR_FACTOR          = 10        
    MIN_PPM = 200 
    MAX_PPM = 10000
    LABEL = "MQ6"

    def __init__(self):
        self.sensorNumber = 6
        
        #format for array: [x, y, slope, min_Rs/Ro, max_Rs/Ro]       
        self.gases = {
                    "CH4":[2.3,0.2,-0.28,0.54,1.6],
                    "LPG":[2.3,0.3,-0.48,0.3,2],
                    "H2":[2.30,0.77,-0.28,2,5.9],
                    "CO":[2.30,0.95,-0.08,6.5,9],
                    "ALCOHOL":[2.30,0.90,-0.17,4.1,8]
                    }
        super(MQ6PPM, self).__init__(self.gases)