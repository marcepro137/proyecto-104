import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sol", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255))
cv2.putText(img, "Mercurio", (110,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Venus", (180,170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Tierra", (280,170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Luna", (330, 160), cv2.FONT_HERSHEY_COMPLEX, 0.25, (0,0,255))
cv2.putText(img, "Marte", (380,180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Jupiter", (560,50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Saturno", (780,100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Urano", (970,140), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))
cv2.putText(img, "Neptuno", (1100,140), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255))

cv2.imshow("output",img)

cv2.waitKey(0)

cv2.imwrite("Solar_sysytemwithname.jpg",img)