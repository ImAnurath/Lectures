from pathlib import Path
from ultralytics import YOLO
import cv2

# ===== Paths =====
script_dir = Path(__file__).parent
image_folder = script_dir / "captured_images"
results_folder = script_dir / "results"
results_folder.mkdir(exist_ok=True)
model_path = script_dir / "best.pt"

# ===== Load Model =====
model = YOLO(str(model_path))
print("Model loaded successfully.")

# ===== Apply Detection =====
image_paths = list(image_folder.glob("*.jpg"))

for i, img_path in enumerate(image_paths):
    print(f"[{i+1}/{len(image_paths)}] Processing {img_path.name}")

    results = model(str(img_path))
    
    # Save annotated image
    for r in results:
        annotated_img = r.plot()  # NumPy array with boxes drawn
        save_path = results_folder / img_path.name
        cv2.imwrite(str(save_path), annotated_img)

print(f"All detections saved to: {results_folder}")