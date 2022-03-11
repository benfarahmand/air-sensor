import time
import math
from MQFunctions import MQFunctions

class MQ3PPM(MQFunctions):
    LABEL = "MQ3"
    
    # v1                                    
    # RL_VALUE                     = 200      
    # RO_CLEAN_AIR_FACTOR          = 60
    # MIN_PPM = 0.05 #unclear if this is accurate. got it from data sheet.
    # MAX_PPM = 10

    #v2
    RL_VALUE                     = 4.7
    RO_CLEAN_AIR_FACTOR          = 1
    MIN_PPM = 50 #unclear if this is accurate. got it from data sheet.
    MAX_PPM = 500
    

    def __init__(self):
        
        self.sensorNumber = 3

        #format for array: [x, y, slope, min_Rs/Ro, max_Rs/Ro]
        self.gases = {"ALCOHOL":[1.7,-0.74,-0.91,0.022,0.18],
                        "CO":[1.70,-0.05,-0.08,0.75,0.9],
                        "H2":[1.70,-0.05,-0.12,0.68,0.9]}
        super(MQ3PPM, self).__init__(self.gases)