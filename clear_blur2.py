import os
import time

import cv2
import shutil
import random

def is_blur(image, THRESHOLD=85):
    is_Var = False
    start = time.time()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageVar = cv2.Laplacian(gray, cv2.CV_64F).var()
    if imageVar < THRESHOLD:
        is_Var = True
    return imageVar, is_Var


def dir_blur(images_path=r'f:/img2/a/'):
    

    for root, dirs, files in os.walk(images_path):
        for tfile in files:
            if tfile.endswith(".jpg"):
                file = os.path.join(root, tfile)
                
                filexml = os.path.join(root, file.replace('.jpg','.xml'))
                image = cv2.imread(file)
                imageVar, is_Var = is_blur(image)
                if is_Var:
                    # shutil.copy(file, dst_dir+str(random.randint(1,10000))+".jpg")
                    os.remove(file)
                    os.remove(filexml)


if __name__ == '__main__':
    dir_blur()
