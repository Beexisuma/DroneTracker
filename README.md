# DroneTracker
# 🛩️ Drone & Bird Detection with YOLOv11

This project implements a **real-time drone and bird detection system** using the **YOLOv11 object detection framework** with **ByteTrack tracking**.  
It was trained on the [Drone Detection Dataset](https://universe.roboflow.com/yolov12-drone-detection/drone-jrg57) from **Roboflow Universe**, which contains ~11,500 annotated images of drones and birds.

---

## 🚀 Features
- Pre-trained on **Roboflow Universe drone dataset**
- Uses **YOLOv11m** for detection
- Real-time video inference with **tracking (ByteTrack)**
- Works with **webcam, local video, and YouTube streams**
- Exports metrics (Precision, Recall, mAP) for evaluation
- Easily extendable to other datasets & models

---
## 📊 Model Performance
| Metric            | Score |
|-------------------|-------|
| **Precision**     | 0.96  |
| **Recall**        | 0.52  |
| **mAP@50**        | 0.75  |
| **mAP@50-95**     | 0.56  |

---

## ⚖️ Notes on Performance
The model demonstrates strong **precision (96%)** but moderate **recall (52%)**, which reflects its ability to detect drones reliably when visible but with some drop-off during partial occlusion (e.g., smoke, fast movement).

Training was performed on a **single NVIDIA RTX 4070 Super** in a home workstation environment.  
Due to compute constraints:
- Training used the **YOLOv11m (medium) model** rather than the larger **YOLOv11x**.  
- Image size was capped at **512 px**.  
- Training ran for **200 epochs**.  

With access to higher-end GPUs (e.g., 4090/5090), the dataset could support **larger models, higher resolution, and longer training**, likely yielding significant improvements in recall and mAP.

