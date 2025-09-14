from ultralytics import YOLO
import torch

def main():
    # Force cuda
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("Using device:", device)


    # Resume training if disrupted during last training
    # model = YOLO(r"runs/detect/train/weights/last.pt")

     # Model I used, nano "n" for fastest training, xl "x" for maximum accuracy
    model = YOLO("yolo11m.pt")

    # Training code
    model.train(
        # Drone Dataset
        data="Drone-8/data.yaml",
        epochs=200,          # this is "extra" epochs for the new run
        imgsz=512,
        batch=-1,            # auto set batch size
        device=0,
        # resume=True,        # Only used if resuming previous run
    )

if __name__ == "__main__":
    main()
