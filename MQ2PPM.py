import time
import math
from MQFunctions import MQFunctions

class MQ2PPM(MQFunctions):

    # v1
    RL_VALUE = 5
    RO_CLEAN_AIR_FACTOR = 9.9
    MIN_PPM = 200 #unclear if this is accurate. got it from data sheet.
    MAX_PPM = 10000
    #v2
    # RL_VALUE                     = 4.7        # define the load resistance on the board, in kilo ohms
    # RO_CLEAN_AIR_FACTOR          = 1     # RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                            # which is derived from the chart in datasheet
    # MIN_PPM = 300 #unclear if this is accurate. got it from data sheet.
    # MAX_PPM = 10000
    LABEL = "MQ2"

    def __init__(self):
        super(MQ135PPM, self).__init__()
        self.sensorNumber = 2
        
        # following values are derived from the logarithmic graphs 
        # from the datasheets format: [x, y, slope], then we can use y=mx+b to figure out
        # then in another equation below we will use these values to determine the ppm
        
        # v1
        self.PropaneCurve = [2.3,0.23,-0.48]    
        self.COCurve = [2.3,0.71,-0.31]    
        self.SmokeCurve = [2.3,0.54,-0.45]    

        #v2
        # self.PropaneCurve = [2.48,-0.66,-0.7]    
        # self.MethaneCurve = [2.48,-0.51,-0.64]     
        # self.AlcoholCurve =[2.48,-0.36,-0.56]   
    
    def getMQPPM(self, raw):
        val = {}
        read = self.MQResistanceCalculation(raw)
        val["LPG"] = self.MQCalcPPM(read/self.Ro, self.PropaneCurve)
        val["CO"] = self.MQCalcPPM(read/self.Ro, self.COCurve)
        val["Smoke"] = self.MQCalcPPM(read/self.Ro, self.SmokeCurve)
        return val