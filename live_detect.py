# import the opencv library
import cv2

# Define a video capture object
vid = cv2.VideoCapture(0)

alg=cv2.CascadeClassifier("PRO-C106-Student-Boilerplate-main/haarcascade_frontalface_default.xml")
while(True):
    # Capture the video frame by frame
    ret, frame = vid.read()
    
    
    grey= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    xywh=alg.detectMultiScale(grey)
    
    print(xywh)
    
    for (x,y,w,h) in xywh:
         
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Display the resulting frame
    cv2.imshow("Web cam", frame)

    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
    
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()