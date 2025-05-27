import requests
import serial
import re
from pathlib import Path
from datetime import datetime
import time

# ===== ESP32 IP Address =====
esp32_ip = "192.168.2.198" # Need to change accordingly from the output terminal.
control_url = f"http://{esp32_ip}/control"
capture_url = f"http://{esp32_ip}/capture"

# ===== Folder for Images =====
script_dir = Path(__file__).parent

folder = script_dir / "captured_images"
folder.mkdir(parents=True, exist_ok=True)
print(f"Folder '{folder}' created successfully.")


# ===== Camera Settings =====
'''
Settings are mostly recommended values for object detection.
Some of them I adjusted myself accordingly to my custom model.
Resolution is intended this way since my model is trained on 640x640 images.
No need to for preprocessing since yolo pads the image by default which is what I would have done.
'''
camera_settings = [
    {"var": "framesize", "val": 6},      # VGA (640x480)
    {"var": "quality", "val": 10},       # Lower = better quality (10–63); 10 is a good balance
    {"var": "brightness", "val": 1},     # -2 to 2
    {"var": "contrast", "val": 2},       # -2 to 2
    {"var": "saturation", "val": 1},     # -2 to 2
    {"var": "awb", "val": 1},            # Auto white balance on
    {"var": "awb_gain", "val": 1},       # Auto white balance gain
    {"var": "aec", "val": 1},            # Auto exposure
    {"var": "aec2", "val": 1},           # DSP AE correction
    {"var": "ae_level", "val": 0},       # Exposure bias (-2 to 2)
    {"var": "agc", "val": 1},            # Auto gain control
    {"var": "gainceiling", "val": 2},    # Gain ceiling (0–6)
    {"var": "hmirror", "val": 0},        # No horizontal flip
    {"var": "vflip", "val": 0},          # No vertical flip
    {"var": "dcw", "val": 1},            # Downsize enable (helps performance)
    {"var": "bpc", "val": 1},            # Black pixel correction
    {"var": "wpc", "val": 1},            # White pixel correction
    {"var": "raw_gma", "val": 1},        # Gamma correction
    {"var": "led_intensity", "val": 0}   # Disable onboard LED if not needed
]

# ===== Set Camera Settings =====
for setting in camera_settings:
    try:
        response = requests.get(control_url, params=setting, timeout=5)
        if response.status_code == 200:
            print(f"{setting['var']} set to {setting['val']} successfully.")
        else:
            print(f"Failed to set {setting['var']}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {setting['var']}: {e}")


# ===== Capture Images Every Second for 5 Minutes =====
duration_seconds = 5 * 60  # 5 minutes
interval = 1  # seconds
total_images = duration_seconds // interval
segment = 1

while True:
    print(f"Starting capture: {total_images} images.\n{duration_seconds/60} minutes with {interval}s interval. \nSegment: {segment}")

    for i in range(total_images):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = folder / f"captured_{timestamp}.jpg"
        
        try:
            response = requests.get(capture_url, timeout=10)
            if response.status_code == 200:
                with open(filename, "wb") as f:
                    f.write(response.content)
                print(f"[{i+1}/{total_images}] Image saved as {filename.name}")
            else:
                print(f"[{i+1}/{total_images}] Failed. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[{i+1}/{total_images}] Request failed:", e)

        time.sleep(interval)

    print("Image capture complete.")

    segment += 1