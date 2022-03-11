import time
import math
from MQFunctions import MQFunctions

class MQ4PPM(MQFunctions):

    RL_VALUE                     = 20 
    RO_CLEAN_AIR_FACTOR          = 4.5

    MIN_PPM = 200
    MAX_PPM = 10000
    LABEL = "MQ4"

    def __init__(self):
        self.sensorNumber = 4
        
        #format for array: [x, y, slope, min_Rs/Ro, max_Rs/Ro]
        self.gases = {"CH4":[3.0,0.0,-0.35,0.45,1.0],
                    "LPG":[3.0,0.2,-0.33,0.75,1.6],
                    "H2":[3.0,0.57,-0.29,1.9,3.7],
                    "CO":[3.0,0.63,-0.09,3.5,4.3],
                    "ALCOHOL":[3.0,0.60,-0.11,3.1,4.0],
                    "SMOKE":[3.0,0.59,-0.18,2.6,3.9]}
        super(MQ4PPM, self).__init__(self.gases)
    