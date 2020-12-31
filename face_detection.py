import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('/content/gdrive/My Drive/file.xml')
# Read the input image
img = cv2.imread('/content/gdrive/My Drive/f/harry.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 2)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #a = a+1
    #cv2.imwrite((imwrite(a,[a,'/content/gdrive/My Drive/f/.jpg']), img[y:y+h, x:x+w])

from google.colab.patches import cv2_imshow
cv2_imshow(img)

cv2.waitKey()

cv2.imwrite('/content/gdrive/My Drive/f/crop.jpg', img[y:y+h, x:x+w])

c = cv2.imread('/content/gdrive/My Drive/f/crop.jpg')
gray = cv2.cvtColor(c, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 2)

cv2_imshow(c)
