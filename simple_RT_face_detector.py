try:
    import numpy as np
    import cv2

except ModuleNotFoundError:

    import subprocess
    import sys

    def install(package):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except:
            print(f"Couldn't download/install necessary module: {package}. Try again or try install it by other way.")

    print("Necessary modules 'numpy' and 'cv2' not found. Wait a minute while they are installing ...")

    install("numpy")
    install("opencv-python")

    print("All the necessary modules were installed.")
    print("Initiating application ... (if it fails, try re-run the application)")

    import numpy as np
    import cv2


def main():

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    vc = cv2.VideoCapture(0)

    print("Press 'ESC' if you need to QUIT application")

    while True:

        there_is_frame, frame = vc.read()

        if not there_is_frame:
            vc.release()
            return

        vc_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(vc_gray, 1.3, 5)

        for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)

        cv2.imshow("Face Detection", frame)

        key = cv2.waitKey(1)

        if key == 27:
            break

    vc.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
