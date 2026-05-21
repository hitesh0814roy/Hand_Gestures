import cv2
from hand_tracking.detector import HandDetector
from gesture_control.gestures import detect_gesture
from gesture_control.volume_control import control_volume
from gesture_control.media_control import control_media
from ui.overlay import draw_ui


def main():
    # Start webcam
    cap = cv2.VideoCapture(0)

    # Set webcam resolution
    cap.set(3, 1280)
    cap.set(4, 720)

    # Initialize hand detector
    detector = HandDetector()

    while True:
        success, frame = cap.read()

        if not success:
            break

        # Flip image for mirror effect
        frame = cv2.flip(frame, 1)

        # Detect hands
        frame, landmarks = detector.find_hands(frame)

        # If hand detected
        if landmarks:

            # Detect gesture
            gesture = detect_gesture(landmarks)

            # Volume control
            control_volume(landmarks)

            # Media control
            control_media(gesture)

            # Draw UI
            draw_ui(frame, gesture)

        # Show webcam window
        cv2.imshow("AirGesture Media Controller", frame)

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()