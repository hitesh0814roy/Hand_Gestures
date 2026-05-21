import cv2
import math


def draw_ui(frame, gesture, landmarks=None):
    """
    Draws UI elements on the webcam frame.
    """

    h, w, _ = frame.shape

    # -----------------------------
    # Gesture Label
    # -----------------------------

    cv2.rectangle(frame, (20, 20), (350, 90), (0, 0, 0), -1)

    cv2.putText(
        frame,
        f"Gesture: {gesture}",
        (40, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # -----------------------------
    # Volume UI
    # -----------------------------

    if landmarks:

        # Thumb tip
        x1, y1 = landmarks[4]

        # Index tip
        x2, y2 = landmarks[8]

        # Draw circles
        cv2.circle(frame, (x1, y1), 12, (255, 0, 255), cv2.FILLED)
        cv2.circle(frame, (x2, y2), 12, (255, 0, 255), cv2.FILLED)

        # Draw line
        cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 255), 3)

        # Distance calculation
        length = math.hypot(x2 - x1, y2 - y1)

        # Convert distance to percentage
        volume_percent = int(
            (length - 30) / (250 - 30) * 100
        )

        # Clamp values
        volume_percent = max(0, min(volume_percent, 100))

        # Volume Bar
        bar_height = int(
            400 - (volume_percent / 100) * 300
        )

        # Draw volume bar outline
        cv2.rectangle(frame, (50, 100), (85, 400), (255, 255, 255), 3)

        # Draw filled volume level
        cv2.rectangle(frame, (50, bar_height), (85, 400), (0, 255, 0), -1)

        # Volume Percentage Text
        cv2.putText(
            frame,
            f"{volume_percent}%",
            (35, 450),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    # -----------------------------
    # Exit Instruction
    # -----------------------------

    cv2.putText(
        frame,
        "Press Q to Exit",
        (w - 250, h - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )