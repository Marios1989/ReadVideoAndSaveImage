import cv2

#Opens the Video File
cap= cv2.VideoCapture('/home/user/PycharmProjects/LOTR.mp4')
i=0
while cap.isOpened:
    ret, frame = cap.read()
    if ret == False:
        break

    if i%100 == 0:
     cv2.imwrite('/home/user/PycharmProjects/Images/kang'+str(i)+'.jpg', frame)
    i+=1

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()