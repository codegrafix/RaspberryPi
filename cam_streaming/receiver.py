
# ToDo
# mkfifo /tmp/fifo.500
# nc 192.168.1.43 2222 > /tmp/fifo.500
import cv2

cap = cv2.VideoCapture("/tmp/fifo.500")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame=cv2.flip(frame,1)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
