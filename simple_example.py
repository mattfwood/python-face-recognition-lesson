import face_recognition

# load an image from a file
image = face_recognition.load_image_file('unknown_photos/sean_sample.png')

# identify face locations
face_locations = face_recognition.face_locations(image)

# print out coordinates
print(face_locations)
