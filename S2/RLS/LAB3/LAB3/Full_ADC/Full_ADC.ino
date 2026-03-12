#include <Arduino.h>

// ====== ADC Sampling Parameters ======
#define ADC_PIN               A0
#define SAMPLE_RATE_HZ        1000
#define SAMPLE_INTERVAL_US    (1000000 / SAMPLE_RATE_HZ)  // 1ms

// ====== FIR Filter ======
#define NUM_TAPS              17
const float fir_coeffs[] = {
    -0.0000000000f,
    -0.0052391811f,
    0.0000000000f,
    0.0232111018f,
    -0.0000000000f,
    -0.0761058457f,
    0.0000000000f,
    0.3076987787f,
    0.5008702926f,
    0.3076987787f,
    0.0000000000f,
    -0.0761058457f,
    -0.0000000000f,
    0.0232111018f,
    0.0000000000f,
    -0.0052391811f,
    -0.0000000000f
};
static float fir_buffer[NUM_TAPS] = { 0 };
static int fir_index = 0;

float fir_filter(float input) {
  fir_buffer[fir_index] = input;
  float output = 0.0f;
  int buf_index = fir_index;
  for (int i = 0; i < NUM_TAPS; i++) {
    output += fir_coeffs[i] * fir_buffer[buf_index];
    buf_index = (buf_index - 1 + NUM_TAPS) % NUM_TAPS;
  }
  fir_index = (fir_index + 1) % NUM_TAPS;
  return output;
}

// ====== DDS (Sine Generator) ======
#define PWM_PIN_DDS        1
#define PWM_RESOLUTION     8      // 8-bit resolution (0-255)
#define PWM_CHANNEL_DDS    0
#define PWM_FREQUENCY_DDS  20000 // 20 kHz base frequency
#define LUT_SIZE           256   // Size of full sine wave period

uint8_t sineLUT[LUT_SIZE];
uint32_t phaseAccumulator = 0;
uint32_t phaseIncrement = 1000;
const uint32_t PHASE_MAX = 0xFFFFFFFF;
float signalFrequency = 1000.0f;    // initial DDS output freq
const float DDS_CLOCK = 10000.0f;    // DDS update rate

// ====== Filtered‑DAC via PWM ======
#define PWM_PIN_FILTER        2
#define PWM_CHANNEL_FILTER    1
#define PWM_FREQUENCY_FILTER  20000 // 20 kHz
#define PWM_RESOLUTION_FILTER 8     // 8‑bit


// ====== Inter‑task Queue ======
QueueHandle_t filteredQueue;

// ====== Function Prototypes ======
void generateSineLUT();
void updatePhaseIncrement(float freq);
void DDSTask(void *param);
void adcTask(void *param);
void dacTask(void *param);

void setup() {
  Serial.begin(115200);
  delay(500);
  Serial.println("Starting ESP32S3 FIR + DDS Demo");

  // --- ADC setup ---
  analogReadResolution(12);
  analogSetAttenuation(ADC_11db);

  // --- PWM for DDS ---
  ledcSetup(PWM_CHANNEL_DDS, PWM_FREQUENCY_DDS, PWM_RESOLUTION);
  ledcAttachPin(PWM_PIN_DDS, PWM_CHANNEL_DDS);

  // --- PWM for Filtered‑DAC ---
  ledcSetup(PWM_CHANNEL_FILTER, PWM_FREQUENCY_FILTER, PWM_RESOLUTION_FILTER);
  ledcAttachPin(PWM_PIN_FILTER, PWM_CHANNEL_FILTER);

  // --- Prepare DDS LUT and phase increment ---
  generateSineLUT();
  updatePhaseIncrement(signalFrequency);

  // --- Create queue for filtered samples ---
  filteredQueue = xQueueCreate(32, sizeof(float));
  if (!filteredQueue) {
    Serial.println("Failed to create queue!");
    while (1) { delay(1000); }
  }
    // --- Create FreeRTOS tasks ---
  xTaskCreate(DDSTask, "DDS Task",   2048, NULL, 1, NULL);
  xTaskCreate(adcTask, "ADC Task",   2048, NULL, 1, NULL);
  xTaskCreate(dacTask, "DAC Task",   2048, NULL, 1, NULL);
}

void loop() {
  // Nothing here—all work happens in tasks
}

// === Generate full‑period sine LUT ===
void generateSineLUT() {
  for (int i = 0; i < LUT_SIZE; i++) {
    float angle = (2.0f * PI) * (float)i / (float)LUT_SIZE;
    sineLUT[i] = (uint8_t)(128 + 127 * sinf(angle));
  }
}

// === Compute phase increment ===
void updatePhaseIncrement(float freq) {
  phaseIncrement = (uint32_t)((freq / DDS_CLOCK) * (PHASE_MAX/4));
  Serial.print("DDS Frequency: ");
  Serial.print(freq);
  Serial.print(" Hz, PhaseInc: ");
  Serial.println(phaseIncrement);
}

// === DDS: outputs sine wave via PWM_CHANNEL_DDS ===
void DDSTask(void *param) {
  while (1) {
    uint8_t idx = phaseAccumulator >> 24; // top 8 bits
    ledcWrite(PWM_CHANNEL_DDS, sineLUT[idx]);
    phaseAccumulator += phaseIncrement;
    vTaskDelay(1); // ~100 µs @ 1 tick/ms
  }
}

// === ADC + FIR Task ===
void adcTask(void *param) {
  while (1) {
    int raw = analogRead(ADC_PIN);
    float volts = raw * (3.3f / 4095.0f);
    float filtered = fir_filter(volts);
    xQueueSend(filteredQueue, &filtered, 0);
    delayMicroseconds(SAMPLE_INTERVAL_US);
  }
}

// === DAC Task: PWM output of filtered signal ===
void dacTask(void *param) {
  float value;
  while (1) {
    if (xQueueReceive(filteredQueue, &value, portMAX_DELAY) == pdTRUE) {
      int out = (int)(value * 255.0f / 3.3f);
      out = constrain(out, 0, 255);
      ledcWrite(PWM_CHANNEL_FILTER, out);
    }
  }
}