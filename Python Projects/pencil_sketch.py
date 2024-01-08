#Pencil Sketch Generator
import cv2
#Reading image
img = cv2.imread("mountain.jpg")
#Converting it to greyscale (B/W)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Inverting the image (negative) (for better working)
img_not = cv2.bitwise_not(gray_img)
#Reducing gaussian blur
blurred = cv2.GaussianBlur(img_not, (21, 21), 0)
#Inverting back to normal
inv_blur = cv2.bitwise_not(blurred)
#Combining grey image and inverted-blurred-grey-image
pencil_sketch = cv2.divide(gray_img, inv_blur, scale=256.0)
#Saving it
cv2.imwrite('pencil_sketch.png', pencil_sketch)