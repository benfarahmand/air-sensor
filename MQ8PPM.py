import time
import math
from MQFunctions import MQFunctions

class MQ8PPM(MQFunctions):
    RL_VALUE                     = 10
    RO_CLEAN_AIR_FACTOR          = 70
    MIN_PPM = 100
    MAX_PPM = 10000
    LABEL = "MQ8"

    def __init__(self):
        self.sensorNumber = 8
        
        #format for array: [x, y, slope, min_Rs/Ro, max_Rs/Ro]    
        self.gases = {"H2":[2.3,0.93,-1.44,0.03,8.5],
                    "LPG":[2.30,1.54,-0.24,13.5,35],
                    "CH4":[2.30,1.72,-0.15,29,53],
                    "CO":[2.30,1.81,-0.12,40,65],
                    "ALCOHOL":[2.30,1.18,-0.47,2.4,15]}
        super(MQ8PPM, self).__init__(self.gases)