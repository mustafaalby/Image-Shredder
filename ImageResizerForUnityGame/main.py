import cv2
import os
import numpy as np
import glob


def main():
    x = input("Can you drop your image or your image folder\n")
    xSplit = x.split('\\')
    # print(len(xSplit))
   # print(xSplit[len(xSplit)-1])
    if ".jpg" in xSplit[len(xSplit)-1] or ".png" in xSplit[len(xSplit)-1]:
        onlyImageResizer(x)
    else:
        imagesInFolderResizer(x)


def onlyImageResizer(imageSRC):
    image = cv2.imread(imageSRC)
    image2 = cv2.resize(image, (960, 540))
    h, w = image2.shape[:2]
    squareHeigh = 270
    squareWidth = 480
    '''cv2.rectangle(image2, (0, 0), (480, 270), color=(255, 255, 0), thickness=2)
    cv2.imshow("ll", image2[0:270, 0:480])
    cv2.rectangle(image2, (480, 270), (960, 540),
                  color=(255, 255, 0), thickness=2)
    cv2.rectangle(image2, (480, 0), (960, 270),
                  color=(255, 255, 0), thickness=2)
    cv2.rectangle(image2, (0, 270), (480, 540),
                  color=(255, 255, 0), thickness=2)
    cv2.imshow("aa", image2)
    '''

    counter = 0
    for i in range(0, w-squareWidth+1, squareWidth):
        for k in range(0, h-squareHeigh+1, squareHeigh):
            # print(i, " ", str(i+squareWidth), ",", k, " ", str(k+squareHeigh))
            # cv2.imshow(str(counter), image2[k:k+squareHeigh, i:i+squareWidth])
            cv2.imwrite(str(counter)+".jpg",
                        image2[k:k+squareHeigh, i:i+squareWidth])
            counter = counter+1
    cv2.waitKey()


def imagesInFolderResizer(folderSRC):
    # r=root, d=directories, f = files
    '''for r, d, f in os.walk(folderSRC):
        for file in f:
            if '.jpg' in file:
                print(file)
    '''
    types = ("*.jpg", "*.png", "*.jpeg")
    files = []
    for types in types:
        files.extend(glob.glob(folderSRC+"/"+types))
    writerMultiple(files)


def writerMultiple(files):
    shredderArray = [3, 4, 5, 6, 8, 9, 10]
    #temp = files[0].split('\\')
    #path = ''.join([temp[i]+'/' for i in range(len(temp)-2)])
    if not os.path.isdir("./output"):
        os.mkdir("./output")
    os.chdir("./output")
    #path = os.getcwd()
    fileCounter = 0
    for index in files:
        if not os.path.isdir("./"+str(fileCounter)):
            os.mkdir("./"+str(fileCounter))
        os.chdir("./"+str(fileCounter))
        fileCounter = fileCounter+1
        imread = cv2.imread(index)
        for i in shredderArray:
            shredderCounter = 0
            print(i)
            if not os.path.isdir("./"+str(i)):
                os.mkdir("./"+str(i))
            os.chdir("./"+str(i))
            shredderCounter = shredderCounter+1
            shrededImageIndex = 0
            for h in range(0, 1080-(1080//i)+1, 1080//i):
                for w in range(0, 1080-(1080//i)+1, 1080//i):
                    cv2.imwrite(str(shrededImageIndex)+".jpg",
                                imread[h:h+(1080//i), w:w+(1080//i)])
                    shrededImageIndex = shrededImageIndex+1
            os.chdir('..')
        os.chdir('..')


main()
