import face_recognition

# load image file
image = face_recognition.load_image_file("my_picture.jpg")

# get landmarks from image
face_landmarks = face_recognition.face_landmarks(image)

# print out list of coordinates for landmarks
print(face_landmarks)
