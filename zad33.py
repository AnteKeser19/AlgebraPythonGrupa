import cv2
import numpy

fotografija='image.jpg'

model=cv2.dnn.readNetFromCaffe('deploy.prototxt','weights.caffemodel')

fotografija_cv2=cv2.imread(fotografija)

(height,width)=fotografija_cv2.shape[:2]

blob_image=cv2.dnn.blobFromImage(cv2.resize(fotografija_cv2, (300,300)),1.0,(300,300),(104.0,177.0,123.0))

model.setInput(blob_image)

detektirana_lica=model.forward()

broj_lica=0

for i in range(0,detektirana_lica.shape[2]):
    okvir=detektirana_lica[0,0,i,3:7]*numpy.array([width,height,width,height])
    (startX,startY,endX,endY)=okvir.astype('int')
    vjerojatnost=detektirana_lica[0,0,i,2]
    if (vjerojatnost>0.2):
        cv2.rectangle(fotografija_cv2, (startX,startY), (endX,endY), (0,255,0), 2)
        broj_lica+=1


print('Pronadjeno je',broj_lica,'lica')
cv2.imshow('Pronadjena lica',fotografija_cv2)
cv2.waitKey()

