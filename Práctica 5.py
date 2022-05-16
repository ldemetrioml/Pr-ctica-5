import cv2
import numpy as np

row = cv2.imread('row.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original",row)

# THRESHOLD_BINARY
retval_binary, threshold_binary= cv2.threshold(row,12,255, cv2.THRESH_BINARY) 
cv2.imshow("Binary",threshold_binary)

# THRESHOLD_BINARY_INV
retval_binary_inv, threshold_binary_inv= cv2.threshold(row,12,255, cv2.THRESH_BINARY_INV)
cv2.imshow("Bin_Inv",threshold_binary_inv)

#THRESHOLD_TRUNC
retval_trunc, threshold_trunc= cv2.threshold(row,12,255, cv2.THRESH_TRUNC)
cv2.imshow("Trunc",threshold_trunc)

#THRESHOLD_TOZERO
retval_tozero, threshold_tozero= cv2.threshold(row,12,255, cv2.THRESH_TOZERO)
cv2.imshow("To Zero",threshold_tozero)

#THRESHOLD_TOZERO_INV
retval_tozero_inv, threshold_tozero_inv= cv2.threshold(row,12,255, cv2.THRESH_TOZERO_INV)
cv2.imshow("TZinv",threshold_tozero_inv)

#Gaus
#gaus= cv2.adaptiveThreshold(row,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115,1)
#cv2.imshow("Gauss",gaus)

#Mean
mean= cv2.adaptiveThreshold(row,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 115,1)
cv2.imshow("Mean",mean)

#Otsu
retval_otsu,otsu=cv2.threshold(row,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("Otsu",otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
