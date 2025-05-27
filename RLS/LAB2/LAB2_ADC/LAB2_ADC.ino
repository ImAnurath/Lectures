// ====== Configuration ======
#define ADC_PIN A0          // Pin D0 (A0)
#define NUM_SAMPLES 1024    // Number of samples
#define SAMPLE_INTERVAL_US 1000  // Sampling interval in microseconds (1ms = 1kHz)

int samples[NUM_SAMPLES];   // Array to store samples

void setup() {
  Serial.begin(115200);     // Fast baud rate for stable transfer
  delay(1000);              // Allow serial to initialize

  analogReadResolution(12); // Use 12-bit ADC (0–4095)
  analogSetAttenuation(ADC_11db); // Suitable for 0–3.3V input range

  Serial.println("Starting ADC Sampling...");
}

void loop() {
  // Collect samples
  for (int i = 0; i < NUM_SAMPLES; i++) {
    samples[i] = analogRead(ADC_PIN);
    delayMicroseconds(SAMPLE_INTERVAL_US);
  }

  // Transmit samples via Serial
  for (int i = 0; i < NUM_SAMPLES; i++) {
    Serial.println(samples[i]); // Just the value for easy plotting
    delayMicroseconds(100);     // Slow down just a bit to avoid USB overrun
  }
}
