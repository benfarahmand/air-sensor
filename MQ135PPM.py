import time
import math
from MQFunctions import MQFunctions

class MQ135PPM(MQFunctions):

    # CALIBRATION_SAMPLE_TIMES = 50

    RL_VALUE                     = 20        # define the load resistance on the board, in kilo ohms
    RO_CLEAN_AIR_FACTOR          = 3.6       # RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                             # which is derived from the chart in datasheet
    MIN_PPM = 10 #unclear if this is accurate. got it from data sheet.
    MAX_PPM = 300
    LABEL = "MQ135"

    def __init__(self):
        super(MQ135PPM, self).__init__()
        self.sensorNumber = 135
        
        # following values are derived from the logarithmic graphs 
        # from the datasheets format: [x, y, slope], then we can use y=mx+b to figure out
        # then in another equation below we will use these values to determine the ppm
        self.AmmoniaCurve = [1.0,0.41,-0.40]    
        self.AlcoholCurve = [1.0,0.29,-0.33]
        self.BenzeneCurve = [1.0,0.20,-0.31]
    
    def getMQPPM(self, raw):
        val = {}
        read = self.MQResistanceCalculation(raw)
        val["NH3"] = self.MQCalcPPM(read/self.Ro, self.AmmoniaCurve)
        val["ALCOHOL"] = self.MQCalcPPM(read/self.Ro, self.AlcoholCurve)
        val["C6H6"] = self.MQCalcPPM(read/self.Ro, self.BenzeneCurve)
        return val