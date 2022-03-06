import time
import math

class MQ2PPM():

    RL_VALUE                     = 5        # define the load resistance on the board, in kilo ohms
    RO_CLEAN_AIR_FACTOR          = 9.83     # RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                            # which is derived from the chart in datasheet

    def __init__(self):
        self.Ro = self.RO_CLEAN_AIR_FACTOR
        
        # following values are derived from the logarithmic graphs 
        # from the datasheets format: [x, y, slope], then we can use y=mx+b to figure out
        # then in another equation below we will use these values to determine the ppm
        self.LPGCurve = [2.3,0.21,-0.47]    
        self.COCurve = [2.3,0.72,-0.34]     
        self.SmokeCurve =[2.3,0.53,-0.44]   
    
    def getMQPPM(self, raw):
        val = {}
        read = self.MQResistanceCalculation(raw)
        val["GAS_LPG"]  = self.MQGetGasPercentage(read/self.Ro, self.LPGCurve)
        val["CO"]       = self.MQGetGasPercentage(read/self.Ro, self.COCurve)
        val["SMOKE"]    = self.MQGetGasPercentage(read/self.Ro, self.SmokeCurve)
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
     
    #########################  MQGetPercentage #################################
    # Input:   rs_ro_ratio - Rs divided by Ro
    #          pcurve      - pointer to the curve of the target gas
    # Output:  ppm of the target gas
    # Remarks: By using the slope and a point of the line. The x(logarithmic value of ppm) 
    #          of the line could be derived if y(rs_ro_ratio) is provided. As it is a 
    #          logarithmic coordinate, power of 10 is used to convert the result to non-logarithmic 
    #          value.
    ############################################################################ 
    def MQGetPercentage(self, rs_ro_ratio, pcurve):
        return (math.pow(10,( ((math.log(rs_ro_ratio)-pcurve[1])/ pcurve[2]) + pcurve[0])))