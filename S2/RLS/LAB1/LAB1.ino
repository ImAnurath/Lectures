const unsigned long sampleIntervalMicros = 1000; // 1000 microseconds = 1 ms

void setup() {
  Serial.begin(115200);
}

void loop() {
  unsigned long startTime = micros();  // Record the starting time
  // Read the analog value from ADC0 (A0)
  int adcValue = analogRead(A0);
  // Print the ADC value to the Serial Monitor
  Serial.println(adcValue);
  delay(100);
  while (micros() - startTime < sampleIntervalMicros) {
    // Do nothing, just wait until 1 ms has passed
  }
}