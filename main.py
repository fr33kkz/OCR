class MyImage:
    def __init__(self, img_name):
        self.img = cv2.imread(img_name)
        self.__name = img_name

    def __str__(self):
        return self.__name
import cv2
import pytesseract
import time
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
pytesseract.pytesseract.tesseract_cmd =  'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
imageName= "sample2.jpg"

img = cv2.imread(imageName)
img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

#filter = np.array([[0,0,-1,0,0],[0,-1,-2,-1,0],[-1,-2,16,-2,-1],[0,-1,-2,-1,0],[0,0,-1,0,0]])
#filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
#img=cv2.filter2D(img,-1,filter)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
print(pytesseract.image_to_string(img))
s = MyImage(imageName)
str(s)
moment=time.strftime("-%Y-%b-%d__%H_%M_%S",time.localtime())
file = open(str(s)+moment+'.txt', "w+")
file.close()
file = open(str(s)+moment+'.txt', "a")
text = pytesseract.image_to_string(img)
file.write(text)
file.close
img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_data(img)
for x,b in enumerate(boxes.splitlines()):
  if x!=0:
        b = b.split()
        if len(b) == 12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img, (x,y), (w+x,h+y), (1,200,255), 3)
            cv2.putText(img, b[11], (x,y-5),cv2.FONT_HERSHEY_DUPLEX,1,(25,25,255),2)
print ("TXT file is created")
img = cv2.resize(img, (1080, 650))
cv2.imshow('Result', img)
cv2.waitKey(0)
##CHARACTER BOXES
#for b in boxes.splitlines():
 #       b = b.split(' ')
  #      x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
   #     cv2.rectangle(img, (x,hImg-y),(w,hImg-h), (1,200,255), 3)
    #    cv2.putText(img, b[0], (x,hImg-y+23),cv2.FONT_HERSHEY_DUPLEX,1,(25,25,255),2)

#WORDS DETECTION
#hImg,wImg,_ = img.shape
#boxes = pytesseract.image_to_data(img)
#for x,b in enumerate(boxes.splitlines()):
 #   if x!=0:
  #      b = b.split()
   #     if len(b) == 12:
    #        x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
     #       cv2.rectangle(img, (x,y), (w+x,h+y), (1,200,255), 3)
      #      cv2.putText(img, b[11], (x,y-5),cv2.FONT_HERSHEY_DUPLEX,1,(25,25,255),2)
##im2 = img.copy()
##file = open("recognized.txt", "w+")
##file.write("")
##file.close()
##file = open("recognized.txt", "a")
##text = pytesseract.image_to_string(im2)
##print(text)
##file.write(text)
##file.close