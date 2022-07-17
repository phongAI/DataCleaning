import imagehash
import os
import PIL
from PIL import Image
import numpy as np
import argparse
import time
ap = argparse.ArgumentParser()
ap.add_argument("-folderName","--folderName",required=True)
Para = ap.parse_args()
duplicatedFolder = "DuplicatedImage"

def main():
    beginTime = time.time()

    #Handling hash
    if(os.path.exists(Para.folderName)):
        duplicatedFile = os.path.join(duplicatedFolder, Para.folderName)
        # Make dir
        os.makedirs(duplicatedFile)
        listImage = sorted(os.listdir(Para.folderName))
        listHash = []
        listName = []
        for imgName in listImage:
            listName.append(imgName)
            imgPath = os.path.join(Para.folderName,imgName)
            "Open image"
            pilImage = Image.open(imgPath)
            "Compute different hash"
            hashImage = imagehash.phash(pilImage)
            "Add hash to list"
            listHash.append(str(hashImage))
        #Get unique hash
        uniqueHash = np.unique(listHash)
        #If no hash name is duplicated
        if len(uniqueHash) == len(listHash):
            print("No duplicated hash")
        else:
            print(f"Total unique file hash is {len(uniqueHash)}/{len(listHash)}")
            listIndex = []
            for uniqueKey in uniqueHash:
                #Get index of duplicated image
                index = np.where(np.array(listHash) == uniqueKey)[0]
                if len(index) > 1:
                    for i in index[1:]:
                        imageName = listName[i]
                        imagePath = os.path.join(Para.folderName,imageName)
                        desPath = os.path.join(duplicatedFile,imageName)
                        #Move image
                        os.rename(imagePath,desPath)
            duration = time.time() - beginTime
            print(f"Move file done in {round(duration,2)}s")
    else:
        raise Exception("Folder empty!")

if __name__ == "__main__":
    main()