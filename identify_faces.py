import face_recognition
import os
from PIL import Image, ImageDraw

known_face_names = []
known_face_encodings = []

# Get all photos from "known faces" directory
for root, dirs, files in os.walk('./known_faces'):
    for filename in files:
        # Create arrays of names and an array of encodings
        known_face_names.append(filename.split('.')[0])
        path = 'known_faces/{}'.format(filename)
        image = face_recognition.load_image_file(path)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)

# Load photo with unknown people
unknown_image = face_recognition.load_image_file(
    'unknown_photos/mexico_group_photo.jpg')

# Find all faces in unknown photo
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Open new image to draw on
new_image = Image.fromarray(unknown_image)
draw = ImageDraw.Draw(new_image)

# Check each face in unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # Compare each face in photo with known faces
    matches = face_recognition.compare_faces(
        known_face_encodings, face_encoding, tolerance=0.5)

    # Name defaults to unknown until a match is made
    name = "Unknown"

    # Set name if match is found
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw rectangle around user's face using the coordinates
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw label to identify face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10),
                    (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5),
              name, fill=(255, 255, 255, 255))

del draw
# open resulting image
new_image.show()
