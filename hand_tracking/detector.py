import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self,
                 mode=False,
                 max_hands=1,
                 detection_confidence=0.7,
                 tracking_confidence=0.7):

        self.mode = mode
        self.max_hands = max_hands

        # MediaPipe Hands
        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )

        # Drawing Utility
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame):

        landmark_list = []

        # Convert BGR → RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process frame
        results = self.hands.process(rgb_frame)

        # Detect hand landmarks
        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                # Draw landmarks
                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

                h, w, c = frame.shape

                for lm in hand_landmarks.landmark:

                    cx = int(lm.x * w)
                    cy = int(lm.y * h)

                    landmark_list.append((cx, cy))

        return frame, landmark_list