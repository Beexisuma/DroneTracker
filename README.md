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


