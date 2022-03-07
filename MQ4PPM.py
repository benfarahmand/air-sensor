import time
import math

class MQ4PPM():

    RL_VALUE                     = 20      # define the load resistance on the board, in kilo ohms
    RO_CLEAN_AIR_FACTOR          = 4.5     # RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                            # which is derived from the chart in datasheet
    MIN_PPM = 200 #unclear if this is accurate. got it from data sheet.
    MAX_PPM = 10000

    def __init__(self):
        self.Ro = self.RO_CLEAN_AIR_FACTOR
        
        # following values are derived from the logarithmic graphs 
        # from the datasheets format: [x, y, slope]
        # then in another equation below we will use these values to determine the ppm
        self.MethaneCurve = [3.0,0.0,-0.35]
        self.LPGCurve = [3.0,0.19,-0.32]
    
    
    def getMQPPM(self, raw):
        val = {}
        read = self.MQResistanceCalculation(raw)
        val["METHANE"]  = self.MQCalcPPM(read/self.Ro, self.MethaneCurve)
        val["GAS_LPG"]  = self.MQCalcPPM(read/self.Ro, self.LPGCurve)
        return val
        
    ######################### MQResistanceCalculation #########################
    # Input:   raw_adc - raw value read from arduino, which represents the voltage
    # Output:  the calculated sensor resistance
    # Remarks: The sensor and the load resistor forms a voltage divider. Given the voltage
    #          across the load resistor and its resistance, the resistance of the sensor
    #          could be derived.
    ############################################################################ 
    def MQResistanceCalculation(self, raw_adc):
        return float(self.RL_VALUE*(1023.0-raw_adc)/float(raw_adc));
     
    #########################  MQCalcPPM #################################
    # Input:   rs_ro_ratio - Rs divided by Ro
    #          pcurve      - pointer to the curve of the target gas
    # Output:  ppm of the target gas
    # Remarks: By using the slope and a point of the line. The x(logarithmic value of ppm) 
    #          of the line could be derived if y(rs_ro_ratio) is provided. As it is a 
    #          logarithmic coordinate, power of 10 is used to convert the result to non-logarithmic 
    #          value.
    ############################################################################ 
    def MQCalcPPM(self, rs_ro_ratio, pcurve):
        return (math.pow(10,( ((math.log(rs_ro_ratio)-pcurve[1])/ pcurve[2]) + pcurve[0])))