import time
import math

class MQFunctions(object):

    CALIBRATION_SAMPLE_TIMES = 50

    def __init__(self, gases):
        self.Ro = self.RO_CLEAN_AIR_FACTOR
        self.calibrationValue = 0.0
        self.calibrationSampleCount = 0
        self.isCalibrationDone = False
        self.data = []
        self.gases = gases
    	#nothing

    def getMQPPM(self, raw):
        val = {}
        read = self.MQResistanceCalculation(raw)
        for gasName, pCurve in self.gases.items():
            #format for pCurve array: [x, y, slope, min_Rs/Ro, max_Rs/Ro]
            # if read/self.Ro < pCurve[3]:
            #     val[gasName] = -2
            # else if read/self.Ro > pCurve[4]:
            #     val[gasName] = -1
            # else:
            val[gasName] = self.MQCalcPPM(read/self.Ro, pCurve)
        return val

    def MQCalibration(self, raw):
        self.calibrationValue += self.MQResistanceCalculation(raw)
        self.calibrationSampleCount +=1
        # print(self.LABEL + ": "+str(self.calibrationSampleCount))
        if self.calibrationSampleCount == self.CALIBRATION_SAMPLE_TIMES:
            self.calibrationValue = self.calibrationValue / self.CALIBRATION_SAMPLE_TIMES

            self.calibrationValue = self.calibrationValue / self.RO_CLEAN_AIR_FACTOR

            self.Ro = self.calibrationValue

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
        #there needs to be a minimum and maximum input range for Rs/Ro, 
        #otherwise the PPM values will fall outside the range of the logarithmic model
        return (math.pow(10,( ((math.log(rs_ro_ratio)-pcurve[1])/ pcurve[2]) + pcurve[0])))