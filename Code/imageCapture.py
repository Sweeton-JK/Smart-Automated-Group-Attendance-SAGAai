import cv2
import os
import time

def capture_image():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Failed to open the camera")
        return

    # Increase brightness
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)

    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        return

    folder_path = "/Users/sweetnotfound/Desktop/Smart-Automated-Group-Attendance-SAGAai/Images/input_images"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = f"{folder_path}/image_{int(time.time())}.jpg"

    cv2.imwrite(filename, frame)

    cap.release()

    print(f"Image captured and saved as {filename}")


def main():
    interval = 5

    while True:
        capture_image()
        time.sleep(interval)


if __name__ == "__main__":
    main()
