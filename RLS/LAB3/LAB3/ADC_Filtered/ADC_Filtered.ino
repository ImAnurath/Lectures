// ====== Configuration ======
#define ADC_PIN A0          // Pin D0 (A0)
#define NUM_SAMPLES 1024    // Number of samples
#define SAMPLE_INTERVAL_US 1000  // Sampling interval in microseconds (1ms = 1kHz)

int samples[NUM_SAMPLES];   // Array to store samples

// ====== FIR Filter ======
#define NUM_TAPS 17
const float fir_coeffs[] = {
-0.000000000000000002,
-0.005239181063014527,
0.000000000000000004,
0.023211101786365075,
-0.000000000000000011,
-0.076105845748673545,
0.000000000000000017,
0.307698778736744338,
0.500870292577157206,
0.307698778736744394,
0.000000000000000017,
-0.076105845748673587,
-0.000000000000000011,
0.023211101786365072,
0.000000000000000004,
-0.005239181063014533,
-0.000000000000000002,
};

float fir_buffer[NUM_TAPS] = {0};
int fir_index = 0;

float fir_filter(float input) {
    fir_buffer[fir_index] = input;
    float output = 0.0f;
    int buf_index = fir_index;

    for (int i = 0; i < NUM_TAPS; i++) {
        output += fir_coeffs[i] * fir_buffer[buf_index];
        buf_index = (buf_index - 1 + NUM_TAPS) % NUM_TAPS; // circular indexing
    }

    fir_index = (fir_index + 1) % NUM_TAPS;
    return output;
}
// ====== Rest of ADC ======
void setup() {
  Serial.begin(115200);     // Fast baud rate for stable transfer
  delay(1000);              // Allow serial to initialize

  analogReadResolution(12); // Use 12-bit ADC (0–4095)
  analogSetAttenuation(ADC_11db); // Suitable for 0–3.3V input range

  Serial.println("Starting ADC Sampling...");
}

void loop() {
  // Collect and filter samples
  for (int i = 0; i < NUM_SAMPLES; i++) {
    int raw = analogRead(ADC_PIN);          // Read 12-bit value (0–4095)
    float voltage = raw * (3.3 / 4095.0);    // Convert to float voltage (optional)

    float filtered = fir_filter(voltage);    // Apply FIR filter

    Serial.println(filtered, 6);             // Print filtered result
    delayMicroseconds(SAMPLE_INTERVAL_US);  // Wait for next sample
  }
}

