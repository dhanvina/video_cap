import cv2

face_id=input('enter your id : ')
cam = cv2.VideoCapture(0);
faceDetect=cv2.CascadeClassifier('C:/Users/Dhanvina/Documents/face_detection/haarcascades/haarcascade_frontalface_default.xml');
# count=0

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5);
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        img_name = f"{face_id}{img_counter}.png"
        if k % 256 == 32:
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
cam.release()

cv2.destroyAllWindows()
