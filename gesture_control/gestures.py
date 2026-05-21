import math


def detect_gesture(landmarks):
    """
    Detects hand gestures based on landmark positions.
    Returns gesture name as string.
    """

    if not landmarks:
        return "No Hand"

    # Fingertip landmark IDs
    THUMB_TIP = 4
    INDEX_TIP = 8
    MIDDLE_TIP = 12
    RING_TIP = 16
    PINKY_TIP = 20

    # Finger lower joint IDs
    INDEX_DIP = 6
    MIDDLE_DIP = 10
    RING_DIP = 14
    PINKY_DIP = 18

    # Get finger positions
    thumb = landmarks[THUMB_TIP]
    index = landmarks[INDEX_TIP]
    middle = landmarks[MIDDLE_TIP]
    ring = landmarks[RING_TIP]
    pinky = landmarks[PINKY_TIP]

    # -----------------------------
    # Finger State Detection
    # -----------------------------

    fingers = []

    # Thumb
    if thumb[0] > landmarks[3][0]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    fingers.append(1 if index[1] < landmarks[INDEX_DIP][1] else 0)
    fingers.append(1 if middle[1] < landmarks[MIDDLE_DIP][1] else 0)
    fingers.append(1 if ring[1] < landmarks[RING_DIP][1] else 0)
    fingers.append(1 if pinky[1] < landmarks[PINKY_DIP][1] else 0)

    total_fingers = fingers.count(1)

    # -----------------------------
    # Gesture Detection
    # -----------------------------

    # Open Palm
    if total_fingers == 5:
        return "PLAY/PAUSE"

    # Fist
    elif total_fingers == 0:
        return "MUTE"

    # Peace Sign
    elif fingers[1] == 1 and fingers[2] == 1 and total_fingers == 2:
        return "VOLUME MODE"

    # Swipe gestures placeholder
    # (Can improve later using motion tracking)

    return "UNKNOWN"