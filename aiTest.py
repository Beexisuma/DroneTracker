import torch
from ultralytics import YOLO

# Trained model path, constant
MODEL_PATH = "runs/detect/train/weights/best.pt"

def main():
    # Force Cuda
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("Using device:", device)

    # Load model
    model = YOLO(MODEL_PATH)

    # Optional Loop due to short test video, demonstrates capabilities better
    while True:
        # Play Video with tracking model engaged
        results = model.track(
            source='drone3.mov', # My source, any video format will do
            show=True, # Show video
            tracker='bytetrack.yaml', # Bytetrack for better object tracking through occlusion
            conf=0.7 # 70% confidence before recognition to reduce false positives
        )


    # Optional Validation Code
    # metrics = model.val(data="Drone-8/data.yaml", conf=0.3)
    # print(metrics)

if __name__ == "__main__":
    main()
