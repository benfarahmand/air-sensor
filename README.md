# air-sensor
 Working on an air quality sensor with MQ-2, MQ-3, MQ-4, MQ-5, MQ-6, MQ-7, MQ-8, MQ-9, and MQ-135

 I went through all the data sheets and calculated the y=mx+b values for the relationship between R_L/R_O and PPM. You can see my work here: https://docs.google.com/spreadsheets/d/1-GPwW0J7FQ4SDkxI_SbeonQL1ulgRazS-9uETGk-KJg/edit?usp=sharing

Hardware:
- Raspberry pi 2 v1.1
- Mega2560 R3
- Sensors: MQ-2, MQ-3, MQ-4, MQ-5, MQ-6, MQ-7, MQ-8, MQ-9, and MQ-135
- PSU: 5V 10AMP

To Do:
- IN PROGRESS: create gui that visualizes the data
- IN PROGRESS: better understand how calibration works to set the Ro value
- implement equation to scale Rs/Ro based on temperature and humidity
- need to connect the temperature and humidity sensor
- get a carbon dioxide sensor
- get a Particulate Matter sensor
- connect 800x480 5-inch touch display


Credits:
- To understand how to convert voltage values to PPM, I borrowed from https://sandboxelectronics.com/?p=165
- Also looked at this code: https://github.com/shubham0490/MQ-sensor-ppm-conversion