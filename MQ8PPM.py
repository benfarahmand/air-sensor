import time
import math

class MQ8PPM():

    CALIBRATION_SAMPLE_TIMES = 50

    RL_VALUE                     = 4.7#10        # define the load resistance on the board, in kilo ohms
    RO_CLEAN_AIR_FACTOR          = 1#70        # RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                             # which is derived from the chart in datasheet
    MIN_PPM = 100 #unclear if this is accurate. got it from data sheet.
    MAX_PPM = 10000
    LABEL = "MQ8"

    def __init__(self):
        self.Ro = self.RO_CLEAN_AIR_FACTOR
        self.calibrationValue = 0.0
        self.calibrationSampleCount = 0
        self.isCalibrationDone = False
        self.sensorNumber = 8
        
        # following values are derived from the logarithmic graphs 
        # from the datasheets format: [x, y, slope], then we can use y=mx+b to figure out
        # then in another equation below we will use these values to determine the ppm
        
        #something is off with these numbers from the datasheet
        #found a different data sheet for mq8 with a different curve, trying that instead
        # self.H2Curve = [2.3,0.93,-1.44] 
        self.H2Curve = [2.0,-0.6,-0.4]#data sheet from sparkfun

    
    def getMQPPM(self, raw):
        val = {}
        read = self.MQResistanceCalculation(raw)
        val["H2"] = self.MQCalcPPM(read/self.Ro, self.H2Curve)
        return val

    def MQCalibration(self, raw):
        self.calibrationValue += self.MQResistanceCalculation(raw)
        self.calibrationSampleCount +=1
        print(self.LABEL + ": "+str(self.calibrationSampleCount))
        if self.calibrationSampleCount == self.CALIBRATION_SAMPLE_TIMES:
            self.calibrationValue = self.calibrationValue / self.CALIBRATION_SAMPLE_TIMES

            self.calibrationValue = self.calibrationValue / self.RO_CLEAN_AIR_FACTOR

            self.Ro = self.calibrationValue

            print("Calibration is done...")
            print(self.LABEL + " Ro= "+str(self.Ro)+" kohm")

            self.isCalibrationDone=True
        
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