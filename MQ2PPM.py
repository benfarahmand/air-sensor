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
    RL_VALUE                     = 4.7        # define the load resistance on the board, in kilo ohms
    RO_CLEAN_AIR_FACTOR          = 1     # RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                           # which is derived from the chart in datasheet
    MIN_PPM = 300 
    MAX_PPM = 10000
    LABEL = "MQ2"

    def __init__(self):
        
        self.sensorNumber = 2
        
        # following values are derived from the logarithmic graphs 
        # from the datasheets format: [x, y, slope], then we can use y=mx+b to figure out
        # then in another equation below we will use these values to determine the ppm
        #v1
        # self.gases = {"LPG":[2.3,0.23,-0.48],
        #             "CO":[2.3,0.71,-0.31],
        #             "Smoke":[2.3,0.54,-0.45]}

        #v2
        self.gases = {"LPG":[2.3,0.23,-0.48],
                    "CH4":[2.3,0.71,-0.31],
                    "ALCOHOL":[2.3,0.54,-0.45]}
        super(MQ2PPM, self).__init__(self.gases)
        # v1
        # self.PropaneCurve = [2.3,0.23,-0.48]    
        # self.COCurve = [2.3,0.71,-0.31]    
        # self.SmokeCurve = [2.3,0.54,-0.45]    

        #v2
        # self.PropaneCurve = [2.48,-0.66,-0.7]    
        # self.MethaneCurve = [2.48,-0.51,-0.64]     
        # self.AlcoholCurve =[2.48,-0.36,-0.56]   
