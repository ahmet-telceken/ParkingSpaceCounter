import cv2
import pickle
import cvzone
import numpy as np

#Video feed
cap = cv2.VideoCapture('C:\Calismalar\ParkingSpaceCounter\\videos\carPark.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 107, 48

def checkParkingSpace(imgPro):

    #Sessin 5
    spaceCounter = 0


    for pos in posList:
        x,y = pos
        #cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

        #imgCrop
        imgCrop = imgPro[y:y+height, x:x+width]
        #cv2.imshow(str(x*y), imgCrop)

        #   **Session 3**
        # We need to count the pixels, how many pixels each of these car spaces has.
        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img, str(count), (x, y+height-5), scale= 1.5, thickness = 2, offset=0)

        # if count < 800 then color is green = empty,
        # otherwise parkspace is not empty = red
        if count < 900:
            color = (0,255,0)
            thickness = 5
            spaceCounter +=1
        else:
            color = (0, 0, 255)
            thickness = 2
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 5), scale=1.5, thickness=2, offset=0)

        #   **Session 3 End**

    cvzone.putTextRect(img, f'Free:{spaceCounter} / {len(posList)}', (100,50), scale=3, thickness=5, offset=20, colorR=(0,200,0))

while True:

    #For loop (video)
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    success, img = cap.read()

    #   **Session 2**
    # we need to tell whether this region has a car present or not
    # we can do that by looking at its pixel count
    # conver this iamge into a binary iamges
    # based on its edges and corners
    # if it doesnt have a lot of edges or corners
    # then if its plain image

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converted Gray
    imgBlur = cv2.GaussianBlur(imgGray, (3,3), 1) #Blur
    #For binary image
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3,3), np.int8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations = 1) #the best form for count pixel
    #   **Session2 End**

    checkParkingSpace(imgDilate)

    #for pos in posList: # for rectangle which is from pickle file
        #cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    #cv2.imshow("ImageBlur", imgBlur)
    #cv2.imshow("ImageThresh", imgThreshold)
    #cv2.imshow("ImageMedian", imgMedian)
    cv2.imshow("imgDilate", imgDilate)
    cv2.waitKey(10)
