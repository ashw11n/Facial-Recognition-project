# initial face detection: printing out position of faces in a given picture
from PIL import Image, ImageDraw
import face_recognition

# loading image file
image = face_recognition.load_image_file("usingpic.PNG")

face_locations = face_recognition.face_locations(image)

print(" {} faces have been discovered within the selected image").format(len(face_locations))

# draw boxes over image
pil_image = Image.fromarray(face_image)
draw = ImageDraw.draw(pil_image)


# face_location is renamed location
for location in face_locations:
    # prints face location for faces found in image
    top, right, bottom, left = location
    print("A face has been found in the stated pixel locations: Top: {}, Right: {}, Bottom {}, Left {}".format(top,right,bottom,left))

    #below commented code cuts faces out of picture and prints them seperately [feature]
    '''
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
    '''

    #instead of printing out faces put boxes on faces in picture
    draw.rectangle(((left, top), (right, bottom)), outline =(0, 255, 0)


pil_image.show()


