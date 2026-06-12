import cv2
import mediapipe as mp
import pyautogui
import math

# Webcam
cap = cv2.VideoCapture(0)

# Screen size
screen_width, screen_height = pyautogui.size()

# MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

draw = mp.solutions.drawing_utils

while True:
    success, frame = cap.read()

    if not success:
        print("Camera not detected")
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    h, w, _ = frame.shape

    if result.multi_hand_landmarks:

        for hand_landmarks in result.multi_hand_landmarks:

            draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Index Finger Tip
            index = hand_landmarks.landmark[8]

            # Thumb Tip
            thumb = hand_landmarks.landmark[4]

            ix, iy = int(index.x * w), int(index.y * h)
            tx, ty = int(thumb.x * w), int(thumb.y * h)

            # Move Mouse
            mouse_x = screen_width * index.x
            mouse_y = screen_height * index.y

            pyautogui.moveTo(mouse_x, mouse_y)

            # Click Gesture
            distance = math.hypot(tx - ix, ty - iy)

            if distance < 25:
                pyautogui.click()
                pyautogui.sleep(0.3)

            cv2.circle(frame, (ix, iy), 10, (0, 255, 0), -1)
            cv2.circle(frame, (tx, ty), 10, (255, 0, 0), -1)

    cv2.imshow("AI Virtual Mouse", frame)

    key = cv2.waitKey(1)

    if key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()