# mediapipe==0.8.7.1
# cvzone==1.4.1
# pynput==1.7.3
# todo = Fix the area of the bounding box and only accept it from a particular area/distance

import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
# DETECTION CONFIDENCE by default it is 0.5 but we want more accuracy
keys = [["1", "2", "3", '#'],
        ["4", "5", "6", '0'],
        ['7', '8', '9', '*']]
# EACH LINE IS A DIFFERENT LIST

finalText = ""


keyboard = Controller()


def drawALL(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0],
                                button.size[1]), 20, rt=0)
        cv2.rectangle(img, button.pos, (x+w, y+h), (225, 0, 255),  cv2.FILLED)
        cv2.putText(img, button.text, (x+20, y+65),
                    cv2.FONT_HERSHEY_PLAIN,
                    4, (255, 255, 255), 4)
        # text,location,font,scale,color,thickness
    return img

# IF YOU WANT TO MAKE THE KEYS TRANSPARENT 
# def drawALL(img, buttonList):
#    imgNew = np.zeros_like(img, np.uint8)
#    for button in buttonList:
#        x, y = button.pos

#        cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0],
#                                   button.size[1]),20, rt=0)

#        cv2.rectangle(img, button.pos, (x+button.size[0], y+button.size[1]),
#                      (225, 0, 255),  cv2.FILLED)

#        cv2.putText(img, button.text, (x+20, y+65),
#                    cv2.FONT_HERSHEY_PLAIN,
#                    4, (255, 255, 255), 4)

#    out = img.copy()
#    alpha = 0.5
#    mask = imgNew.astype(bool)
#    print(mask.shape)
#    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
#    return out


class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text


buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100*j+50, 100*i+50], key))

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist, bboxInfo = detector.findPosition(img)
    # Scale the output image
    # scale_percent = 200  # percent of original size
    #width = int(img.shape[1] * scale_percent / 100)
    #height = int(img.shape[0] * scale_percent / 100)
    #dim = (width, height)
    #img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    drawALL(img, buttonList)

    if lmlist:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmlist[8][0] < x+w and y < lmlist[8][1] < y+h:
                cv2.rectangle(img, (x-5, y-5), (x+w+5, y+h+5),
                              (175, 0, 175),  cv2.FILLED)
                cv2.putText(img, button.text, (x+20, y+65),
                            cv2.FONT_HERSHEY_PLAIN,
                            4, (255, 255, 255), 4)
                # wheb u want to ignore parameter then we use _ #to not show like distance
                l, _, _, = detector.findDistance(8, 12, img, draw=False)
                print(l)

                # WHEN CLICKED
                if l < 30:
                    keyboard.press(button.text)
                    cv2.rectangle(img, button.pos, (x+w, y+h),
                                  (0, 225, 0),  cv2.FILLED)
                    cv2.putText(img, button.text, (x+20, y+65),
                                cv2.FONT_HERSHEY_PLAIN,
                                4, (255, 255, 255), 4)

                    finalText += button.text
                    sleep(0.15)

            cv2.rectangle(img, (50, 350), (700, 450),
                          (175, 0, 175),  cv2.FILLED)
            cv2.putText(img, finalText, (60, 430),
                        cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    cv2.imshow("Image", img)

    cv2.waitKey(1)
