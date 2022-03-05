int MQ2 = A0;
int MQ3 = A1;
int MQ4 = A2;
int MQ5 = A3;
int MQ6 = A4;
int MQ7 = A5;
int MQ8 = A6;
int MQ9 = A7;
int MQ135 = A8;

void setup() {
  pinMode(MQ2, INPUT);
  pinMode(MQ3, INPUT);
  pinMode(MQ4, INPUT);
  pinMode(MQ5, INPUT);
  pinMode(MQ6, INPUT);
  pinMode(MQ7, INPUT);
  pinMode(MQ8, INPUT);
  pinMode(MQ9, INPUT);
  pinMode(MQ135, INPUT);
  Serial.begin(115200);
}

void loop() {
  int mq2Sensor = analogRead(MQ2);
  int mq3Sensor = analogRead(MQ3);
  int mq4Sensor = analogRead(MQ4);
  int mq5Sensor = analogRead(MQ5);
  int mq6Sensor = analogRead(MQ6);
  int mq7Sensor = analogRead(MQ7);
  int mq8Sensor = analogRead(MQ8);
  int mq9Sensor = analogRead(MQ9);
  int mq135Sensor = analogRead(MQ135);

  Serial.println("-----------------");
  Serial.print("  MQ2: ");
  Serial.print(mq2Sensor);
  Serial.println(" - LPG, Propane and Hydrogen");
  Serial.print("  MQ3: ");
  Serial.print(mq3Sensor);
  Serial.println(" - Alcohol, Ethanol");
  Serial.print("  MQ4: ");
  Serial.print(mq4Sensor);
  Serial.println(" - Methane, Natural Gas");
  Serial.print("  MQ5: ");
  Serial.print(mq5Sensor);
  Serial.println(" - LPG, Natural Gas");
  Serial.print("  MQ6: ");
  Serial.print(mq6Sensor);
  Serial.println(" - LPG, Iso-butane, Propane");
  Serial.print("  MQ7: ");
  Serial.print(mq7Sensor);
  Serial.println(" - Carbon Monoxide");
  Serial.print("  MQ8: ");
  Serial.print(mq8Sensor);
  Serial.println(" - Hydrogen");
  Serial.print("  MQ9: ");
  Serial.print(mq9Sensor);
  Serial.println(" - Methane, Propane and CO");
  Serial.print("MQ135: ");
  Serial.print(mq135Sensor);
  Serial.println(" - NH3, NOx, alcohol, Benzene, smoke, CO2");
  delay(2000);
}
