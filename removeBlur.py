import os
import argparse
import cv2
import time
ap = argparse.ArgumentParser()
ap.add_argument("-threshold","--threshold",default=30)
ap.add_argument("-folderName","--folderName",required=True)
Para = ap.parse_args()
blurFolder = "BlurImages"
def LaplacianValue(imagePath):
    if os.path.exists(imagePath):
        img = cv2.imread(imagePath)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        value = cv2.Laplacian(img,cv2.CV_64F).var()
        return value

def main():
    beginTime = time.time()
    countBlur = 0

    #Check file exist
    if os.path.exists(Para.folderName):
        # Make dir
        BlurFile = os.path.join(blurFolder,Para.folderName)
        os.makedirs(BlurFile)

        totalImage = len(os.listdir(Para.folderName))
        # Handle blur image
        for imageName in os.listdir(Para.folderName):
            imagePath = os.path.join(Para.folderName,imageName)
            laplaValue = LaplacianValue(imagePath)
            if laplaValue < int(Para.threshold):
                countBlur += 1
                #Move file
                desPath = os.path.join(BlurFile,imageName)
                os.rename(imagePath,desPath)
        print(f"Total {countBlur}/{totalImage} blurry image")
        duration = time.time() - beginTime
        print(f"Time for processing {round(duration,2)}s")
    else:
        raise Exception("Folder empty!")


if __name__ == "__main__":
    main()