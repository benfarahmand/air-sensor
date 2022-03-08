import time
import math
from MQFunctions import MQFunctions

class MQ4PPM(MQFunctions):

    RL_VALUE                     = 20      # define the load resistance on the board, in kilo ohms
    RO_CLEAN_AIR_FACTOR          = 4.5     # RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                            # which is derived from the chart in datasheet
    MIN_PPM = 200 #unclear if this is accurate. got it from data sheet.
    MAX_PPM = 10000
    LABEL = "MQ4"

    def __init__(self):
        self.sensorNumber = 4
        
        # following values are derived from the logarithmic graphs 
        # from the datasheets format: [x, y, slope]
        # then in another equation below we will use these values to determine the ppm
        # self.MethaneCurve = [3.0,0.0,-0.35]
        # self.LPGCurve = [3.0,0.19,-0.32]
        self.gases = {"LPG":[3.0,0.19,-0.32],
                    "CH4":[3.0,0.0,-0.35]}
        super(MQ4PPM, self).__init__(self.gases)
    
    
    # def getMQPPM(self, raw):
    #     val = {}
    #     read = self.MQResistanceCalculation(raw)
    #     val["LPG"]  = self.MQCalcPPM(read/self.Ro, self.LPGCurve)
    #     val["CH4"]  = self.MQCalcPPM(read/self.Ro, self.MethaneCurve)
    #     return val