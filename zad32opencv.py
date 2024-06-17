# python3 -m pip install opencv-python

import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
fotografija=cv2.imread('Algebra_greyp.jpg')
cb_fotografija=cv2.cvtColor(fotografija, cv2.COLOR_BGR2GRAY)

prepoznata_lica=face_cascade.detectMultiScale(
    cb_fotografija,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30)
)

print(f'Pronađeno je {len(prepoznata_lica)} lica')

print(prepoznata_lica[0])

for (x, y, w, h) in prepoznata_lica:
    cv2.rectangle(fotografija, (x,y), (x+w,y+h), (0,255,0),2)

cv2.imshow('Pronadjena lica', fotografija)

cv2.waitKey()

#vlastita fotografija / s interneta s puno lica
#fotografija slikana iz kuta