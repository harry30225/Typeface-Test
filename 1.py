import numpy as np
import cv2 as cv

img = cv.imread('./input.jpg',1)
ret,thresh = cv.threshold(img,127,255,0)
im2,contours,hierarchy = cv.findContours(thresh, 1, 2)

ans = []

for cnt in contours:
    M = cv.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    x,y,w,h = cv.boundingRect(cnt)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    a = []
    a.append(cx)
    a.append(cy)
    a.append(w)
    a.append(h)
    ans.append(a)

ans = np.array(ans)

for a in ans:
    print(a)
