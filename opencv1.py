import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)

    # for exit
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    print('Just another print statement')

    # for capture
    elif k%256 == 32:
        # SPACE pressed
        # whenever space is pressed the video frame is captured
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()


#captures images from video by clicking space bar
