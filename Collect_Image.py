import cv2 # opencv
import time # to take a break during collection
import os # work with file
import uuid # to name image file

images_path = 'Tensorflow/workspace/images/collected_images'

# set up the label (signs that i am going to collect)
labels = ['hello', 'thanks', 'yes', 'no', 'i_love_you']
num_imgs = 15

# to collect images
for label in labels:
    dir_path = os.path.join(images_path, label)
    os.makedirs(dir_path, exist_ok=True)
    cap =  cv2.VideoCapture(0)
    print("collecting images for {}".format(label))
    time.sleep(5)

    for img_num in range(num_imgs):
        ret, frame = cap.read()
        img_name = os.path.join(images_path, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(img_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
    cap.release()