import cv2

# Load an image (make sure this image file is in the same folder as your script)
img = cv2.imread('your_image.jpg')  # replace 'your_image.jpg' with your actual image filename

# Show the image in a window
cv2.imshow('Test Image', img)
cv2.waitKey(0)  # waits until you press any key
cv2.destroyAllWindows()
