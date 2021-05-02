import cv2


def draw_found_faces(detected, image, color: tuple):
    for (x, y, width, height) in detected:
        cv2.rectangle(
            image,
            (x, y),
            (x + width, y + height),
            color,
            thickness=2
        )


video_capture = cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# eye_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

while True:

    _, frame = video_capture.read()

    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detected_faces = face_cascade.detectMultiScale(
        image=grayscale_image, scaleFactor=1.3, minNeighbors=4)
    # detected_eyes = eye_cascade.detectMultiScale(
    #     image=grayscale_image, scaleFactor=1.3, minNeighbors=4)
    draw_found_faces(detected_faces, frame, (0, 200, 0))
   # draw_found_faces(detected_eyes, frame, (0, 255, 0))

    # Display the updated frame as a video stream
    cv2.imshow('Webcam Face Detection', frame)
    keyCode = cv2.waitKey(1)

    if cv2.getWindowProperty('Webcam Face Detection', cv2.WND_PROP_VISIBLE) < 1:
        break


video_capture.release()


cv2.destroyAllWindows()
