import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("camera didn’t open, rip")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("couldn’t read from cam, meh")
        break

    cv2.imshow("webcam", frame)

    # straight up check the key without masking
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
