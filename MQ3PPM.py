import time
import math
from MQFunctions import MQFunctions

class MQ3PPM(MQFunctions):
    LABEL = "MQ3"
    
    # v1                                    
    RL_VALUE                     = 200      
    RO_CLEAN_AIR_FACTOR          = 60
    MIN_PPM = 0.05 #unclear if this is accurate. got it from data sheet.
    MAX_PPM = 10

    #v2
    # RL_VALUE                     = 4.7
    # RO_CLEAN_AIR_FACTOR          = 1
    # MIN_PPM = 50 #unclear if this is accurate. got it from data sheet.
    # MAX_PPM = 500
    

    def __init__(self):
        
        self.sensorNumber = 3
        # following values are derived from the logarithmic graphs 
        # from the datasheets format: [x, y, slope]
        # then in another equation below we will use these values to determine the ppm
        self.gases = {"ALCOHOL":[-1.0,0.36,-0.64]}
        super(MQ3PPM, self).__init__(self.gases)
        # self.AlcoholCurve = [-1.0,0.36,-0.64] #v1
        # self.AlcoholCurve = [1.7,-0.74,-0.91] #v2
    
    # def getMQPPM(self, raw):
    #     val = {}
    #     read = self.MQResistanceCalculation(raw)
    #     val["ALCOHOL"]  = self.MQCalcPPM(read/self.Ro, self.AlcoholCurve)
    #     return val