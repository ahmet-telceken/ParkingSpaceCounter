# First ; Select and deselect parkin spaces
# Put them all in a list
# Once we select, we are going to save it

import cv2
import pickle #for save all the places, positions


# Check pickle file if it's exist then load
# if not exist, then create new posList
# posList = position of parking space
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []
width, height = 107, 48



# 3- Detect the mouse click
def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1+width and y1 < y < y1+height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)



while True:
    img = cv2.imread('C:\Calismalar\ParkingSpaceCounter\\videos\carParkImg.png')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
    #cv2.rectangle(img, (50,100), (277,500), (255, 0, 255), 2)
    cv2.imshow("Image", img)
    # 4- We can display , what we have created(rectangle)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)