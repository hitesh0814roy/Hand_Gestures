import math
import pyautogui


# Store previous volume level
previous_level = 0


def control_volume(landmarks):
    """
    Control volume using thumb-index distance.
    """

    global previous_level

    if not landmarks or len(landmarks) < 9:
        return

    # Thumb tip
    x1, y1 = landmarks[4]

    # Index tip
    x2, y2 = landmarks[8]

    # Calculate distance
    distance = math.hypot(x2 - x1, y2 - y1)

    # Convert distance into levels
    current_level = int(distance / 20)

    # Increase volume
    if current_level > previous_level:
        pyautogui.press("volumeup")

    # Decrease volume
    elif current_level < previous_level:
        pyautogui.press("volumedown")

    # Update previous level
    previous_level = current_level