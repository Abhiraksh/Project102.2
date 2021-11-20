#Taking a photo 
import cv2

def takePhoto():

    vco = cv2.VideoCapture(0)
    #0 is for accessing webcam and 1 is for accessing the outer camera
    result = True
    while(result):
        ret, frame = vco.read()
        cv2.imwrite("Photo.jpg", frame)
        vco.release()
        cv2.destroyAllWindows()
        print("Photo Taken")
        result = False

takePhoto()