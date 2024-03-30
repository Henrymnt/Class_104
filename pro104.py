import cv2

img=cv2.imread("poster.jpg")
rocket=img[120:360,400:500]
img[0:240,500:600]=rocket

text_toShow='Here is the Image: '
cv2.putText(img, 
            text_toShow,
            (50,250),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX,
            fontScale=1,
            color=(0,0,255)
            )

cv2.imshow('Image', img)
cv2.waitKey(0)