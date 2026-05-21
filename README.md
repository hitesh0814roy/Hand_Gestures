# AirGesture Media Controller

A real-time computer vision project that allows users to control system volume and music playback using hand gestures through a webcam.

---

# Features

- Real-time hand tracking
- Gesture-based volume control
- Play/Pause music
- Next/Previous track control
- Live webcam interface
- Touchless media interaction

---

# Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy
- pycaw

---

# Project Structure

```bash
AirGesture-Media-Controller/
│
├── main.py
├── requirements.txt
├── README.md
│
├── hand_tracking/
│   └── detector.py
│
├── gesture_control/
│   ├── gestures.py
│   ├── volume_control.py
│   └── media_control.py
│
├── ui/
│   └── overlay.py
│
└── utils/
    └── helpers.py
```

---

# Installation

## Clone Repository

```bash
git clone <your-github-repo-link>
cd AirGesture-Media-Controller
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python main.py
```

---

# Controls

| Gesture | Action |
|---|---|
| Thumb + Index Distance | Volume Control |
| Open Palm | Play/Pause |
| Swipe Right | Next Song |
| Swipe Left | Previous Song |
| Fist | Mute |

---

# Requirements

- Python 3.9+
- Webcam
- Windows/Linux/macOS

---

# Future Improvements

- Brightness control
- Air mouse
- AI gesture recognition
- Custom gesture mapping
- Desktop application UI

---

# Author

Hitesh Satvik Roy

---

# License

This project is open-source and free to use.