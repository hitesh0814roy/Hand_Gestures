import time
from pathlib import Path

import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self,
                 mode=False,
                 max_hands=1,
                 detection_confidence=0.7,
                 tracking_confidence=0.7,
                 model_path=None):

        self.mode = mode
        self.max_hands = max_hands
        self.model_path = self._resolve_model_path(model_path)
        self.connections = mp.tasks.vision.HandLandmarksConnections.HAND_CONNECTIONS

        running_mode = (
            mp.tasks.vision.RunningMode.IMAGE
            if self.mode
            else mp.tasks.vision.RunningMode.VIDEO
        )

        options = mp.tasks.vision.HandLandmarkerOptions(
            base_options=mp.tasks.BaseOptions(
                model_asset_path=str(self.model_path)
            ),
            running_mode=running_mode,
            num_hands=self.max_hands,
            min_hand_detection_confidence=detection_confidence,
            min_hand_presence_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence,
        )

        self.landmarker = mp.tasks.vision.HandLandmarker.create_from_options(options)

    def _resolve_model_path(self, model_path):
        if model_path is None:
            project_root = Path(__file__).resolve().parents[1]
            model_path = project_root / "models" / "hand_landmarker.task"

        model_path = Path(model_path).resolve()

        if not model_path.exists():
            raise FileNotFoundError(
                "MediaPipe Hand Landmarker model not found. "
                f"Download hand_landmarker.task and place it at: {model_path}"
            )

        return model_path

    def find_hands(self, frame):

        landmark_list = []

        # Convert BGR to RGB for MediaPipe.
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        if self.mode:
            results = self.landmarker.detect(mp_image)
        else:
            timestamp_ms = int(time.time() * 1000)
            results = self.landmarker.detect_for_video(mp_image, timestamp_ms)

        # Detect hand landmarks
        if results.hand_landmarks:

            for hand_landmarks in results.hand_landmarks:

                self._draw_landmarks(frame, hand_landmarks)

                h, w, c = frame.shape

                for lm in hand_landmarks:

                    cx = int(lm.x * w)
                    cy = int(lm.y * h)

                    landmark_list.append((cx, cy))

        return frame, landmark_list

    def _draw_landmarks(self, frame, hand_landmarks):
        h, w, _ = frame.shape
        points = [
            (int(landmark.x * w), int(landmark.y * h))
            for landmark in hand_landmarks
        ]

        for connection in self.connections:
            cv2.line(
                frame,
                points[connection.start],
                points[connection.end],
                (255, 255, 255),
                2
            )

        for point in points:
            cv2.circle(frame, point, 4, (0, 255, 0), cv2.FILLED)
