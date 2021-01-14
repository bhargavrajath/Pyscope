#define ref_volt 3.3  // MCU ADC reference voltage
#define ADC_res 10    // ADC resolution in bits
#define ch1 A3        // pin used for analog measurement

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(ref_volt*analogRead(ch1)/ADC_res);
  delay(10); // adjust this if you see latency
}
