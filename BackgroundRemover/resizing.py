import cv2
import os

for root, subdirs, files in os.walk('/Users/ozlemserifogullari/Documents/comp437/project/BackgroundRemover/bgimages'):
    for f in files:
        if f.endswith('jpg'):
            # print(f)
            img = cv2.imread('/Users/ozlemserifogullari/Documents/comp437/project/BackgroundRemover/bgimages/' + f)
            img = cv2.resize(img, (640, 480))
            cv2.imwrite('/Users/ozlemserifogullari/Documents/comp437/project/BackgroundRemover/bgimages/'+f, img)
            print(*["Image", f, "is resized to 640 X 480"])
