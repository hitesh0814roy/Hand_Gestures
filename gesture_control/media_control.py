import pyautogui
import time

# Cooldown timer
last_action_time = 0
cooldown = 1  # seconds


def control_media(gesture):
    """
    Controls media playback based on detected gesture.
    """

    global last_action_time

    current_time = time.time()

    # Prevent repeated triggers
    if current_time - last_action_time < cooldown:
        return

    # -----------------------------
    # Media Controls
    # -----------------------------

    if gesture == "PLAY/PAUSE":
        pyautogui.press("playpause")
        print("Play/Pause")

    elif gesture == "NEXT":
        pyautogui.press("nexttrack")
        print("Next Track")

    elif gesture == "PREVIOUS":
        pyautogui.press("prevtrack")
        print("Previous Track")

    elif gesture == "MUTE":
        pyautogui.press("volumemute")
        print("Mute")

    else:
        return

    # Update cooldown timer
    last_action_time = current_time