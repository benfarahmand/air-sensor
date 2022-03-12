import time
import math
from MQFunctions import MQFunctions

class MQ9PPM(MQFunctions):


    RL_VALUE                     = 10        
    RO_CLEAN_AIR_FACTOR          = 10        
    MIN_PPM = 500 
    MAX_PPM = 10000
    LABEL = "MQ9"

    def __init__(self):
        self.sensorNumber = 9
        
        #format for array: [x, y, slope, min_Rs/Ro, max_Rs/Ro]
        self.gases = {"LPG":[2.3,0.3,-0.46,0.33,2],
                    "CO":[2.3,0.2,-0.43,0.8,1.6],
                    "CH4":[2.3,0.48,-0.37,0.7,3]}
        super(MQ9PPM, self).__init__(self.gases)