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

    # checks unicode of the key press to match with the letter q
    if cv2.waitKey(1) == ord('q'):
        break
#i guess this is good practice so why not<>
cap.release()
cv2.destroyAllWindows()
