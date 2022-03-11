import time
import math
from MQFunctions import MQFunctions

class MQ2PPM(MQFunctions):

    # v1
    # RL_VALUE = 5
    # RO_CLEAN_AIR_FACTOR = 9.9
    # MIN_PPM = 200 
    # MAX_PPM = 10000
    #v2
    RL_VALUE                     = 4.7
    RO_CLEAN_AIR_FACTOR          = 1
    MIN_PPM = 300 
    MAX_PPM = 10000

    LABEL = "MQ2"

    def __init__(self):
        
        self.sensorNumber = 2
        
        #v1
        # self.gases = {"LPG":[2.3,0.23,-0.48],
        #             "CO":[2.3,0.71,-0.31],
        #             "Smoke":[2.3,0.54,-0.45]}

        #v2
        #format for array: [x, y, slope, min_Rs/Ro, max_Rs/Ro]
        self.gases = {"LPG":[2.48,-0.66,-0.7, 0.019, 0.22],
                    "CH4": [2.48,-0.51,-0.64, 0.033, 0.31],
                    "ALCOHOL":[2.48,-0.36,-0.56, 0.062, 0.44],
                    "SMOKE":[2.48,-0.57,-0.68, 0.025, 0.27]}
        super(MQ2PPM, self).__init__(self.gases)
