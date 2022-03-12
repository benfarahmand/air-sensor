import time
import math
from MQFunctions import MQFunctions

class MQ135PPM(MQFunctions):

    RL_VALUE                     = 20     
    RO_CLEAN_AIR_FACTOR          = 3.6    
    MIN_PPM = 10
    MAX_PPM = 300
    LABEL = "MQ135"

    def __init__(self):
        self.sensorNumber = 135
        
        #format for array: [x, y, slope, min_Rs/Ro, max_Rs/Ro]
        self.gases = {"NH3":[1.0,0.41,-0.40,0.78,2.6],
                    "ALCOHOL":[1.0,0.29,-0.33,0.73,1.95],
                    "C6H6":[1.0,0.20,-0.31,0.64,1.6],
                    "ACETONE":[1.00,0.18,-0.31,0.59,1.5],
                    "CO2":[1.00,0.38,-0.37,0.8,2.4],
                    "CO":[1.00,0.45,-0.23,1.4,2.8]}
        super(MQ135PPM, self).__init__(self.gases)
    