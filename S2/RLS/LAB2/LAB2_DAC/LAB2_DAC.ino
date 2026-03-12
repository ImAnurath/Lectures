#define PWM_PIN 1
#define PWM_RESOLUTION 8  // 8-bit resolution (0-255)
#define PWM_FREQUENCY 20000  // 20 kHz base frequency
#define LUT_SIZE 256  // Size of full sine wave period

// Create the LUT for full period of sine wave
uint8_t sineLUT[LUT_SIZE];

// DDS parameters
uint32_t phaseAccumulator = 0;
uint32_t phaseIncrement = 1000;
const uint32_t PHASE_MAX = 0xFFFFFFFF;  // 32-bit phase accumulator max value

// Signal parameters
float signalFrequency = 1000.0;  // Initial frequency (Hz)
const float DDS_CLOCK = 10000.0;  // DDS update rate (Hz)


TaskHandle_t DDSTaskHandle;

void setup() {
  Serial.begin(115200);
  while(!Serial);  // Wait for serial connection
  
  // Configure PWM
  ledcSetup(0, PWM_FREQUENCY, PWM_RESOLUTION);
  ledcAttachPin(PWM_PIN, 0);
  
  // Generate full period of sine wave in LUT
  generateSineLUT();
  
  // Calculate initial phase increment based on frequency
  updatePhaseIncrement(signalFrequency);
  
  // Create DDS task
  xTaskCreate(
    DDSTask,          // Function that implements the task
    "DDSTask",        // Text name for the task
    2048,             // Stack size in words
    NULL,             // Parameter passed into the task
    1,                // Priority at which the task is created
    &DDSTaskHandle    // Used to pass out the created task's handle
  );
  
  Serial.println("PWM initialized on pin 1");
  Serial.println("Sine wave LUT generated");
  Serial.println("DDS task started");
}

void generateSineLUT() {
  for (int i = 0; i < LUT_SIZE; i++) {
    // Calculate sine for 0 to 2π (full period)
    float angle = (2.0 * PI) * (float)i / (float)LUT_SIZE;
    // Scale sine value (which is -1 to +1) to fit PWM range (0-255)
    sineLUT[i] = (uint8_t)(128 + 127 * sin(angle));
  }
}

void updatePhaseIncrement(float frequency) {
  // Formula: phaseIncrement = (frequency / DDS_CLOCK) * 2^32
  phaseIncrement = (uint32_t)((frequency / DDS_CLOCK) * PHASE_MAX/4);
  
  Serial.print("Frequency set to: ");
  Serial.print(frequency);
  Serial.print(" Hz, Phase Increment: ");
  Serial.println(phaseIncrement);
}

// DDS Task - Runs continuously to generate samples
void DDSTask(void *parameter) {
  uint32_t lastPrintTime = 0;
  const uint32_t PRINT_INTERVAL = 5000;
  
  while(1) {
    // Get the current time
    uint32_t currentTime = millis();
    
    // Extract LUT index from phase accumulator
    uint8_t lutIndex = phaseAccumulator >> 24;  // Use top 8 bits for indexing
    
    // Get the sine value directly from the LUT
    uint8_t sineValue = sineLUT[lutIndex];
    
    // Output the sample through PWM
    ledcWrite(0, sineValue);
    
    // Increment the phase accumulator
    phaseAccumulator += phaseIncrement;
    
    // Print info periodically
    if (currentTime - lastPrintTime >= PRINT_INTERVAL) {
      Serial.print("Phase Accumulator: ");
      Serial.print(phaseAccumulator);
      Serial.print(", Phase Increment: ");
      Serial.print(phaseIncrement);
      Serial.print(", Frequency: ");
      Serial.print(signalFrequency);
      Serial.println(" Hz");
      
      lastPrintTime = currentTime;
    }
    
    // Small delay for DDS clock rate control
    vTaskDelay(1 / portTICK_PERIOD_MS);
  }
}

void loop() {
  // Main loop can be used to adjust frequency if needed
  delay(10);
}