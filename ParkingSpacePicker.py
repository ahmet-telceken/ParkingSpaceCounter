# First ; Select and deselect parkin spaces
# Put them all in a list
# Once we select, we are going to save it

import cv2 as cv
import pickle #for save all the places, positions

img = cv.imread('C:\Calismalar\ParkingSpaceCounter\\videos\carParkImg.png')

width, height = 107, 48
posList = []

def mouseClick(events, x, y, flags, params):
    if events == cv.EVENT_LBUTTONDOWN:
        posList.append((x, y))


while True:
    # 3- Detect het mouse click
        #def mouseClick tanımlandi
    # 4- We can dsplay , what we have created(rectangle)
    for pos in posList:
        # 2- Create rectangle
        cv.rectangle(img, pos, (pos[0]+width, pos[1]+height), (255, 0, 255), 2)

    cv.imshow('Image', img)
    cv.setMouseCallback("Image", mouseClick)
    cv.waitKey(0)