import os
import pandas as pd


def filesToMerge(dirPath, substringName):
    listOfFilesToMerge = []
    for fileName in os.listdir(dirPath):
        if substringName in fileName:
            pathToFile = os.path.join(dirPath, fileName)
            listOfFilesToMerge.append(pathToFile)
    print("found list of files to merge")
    return listOfFilesToMerge


def mergeFiles(listOfFiles, target):
    combined_csv_file_path = target
    combined_csv = pd.read_csv(listOfFiles[0])
    del listOfFiles[0]
    for f in listOfFiles:
        print("processing file: " + f)
        try:
            combined_csv = pd.concat([pd.read_csv(f), combined_csv])
        except Exception:
            print("for file " + f + " there was exception: " + str(Exception))
    combined_csv.to_csv(combined_csv_file_path, index=False, encoding='utf-8-sig')


pathToDataDir = "/media/frezer02/7D3CDB1B28552965/Data/bert/"
targetDir = pathToDataDir + "output/"
searchedType = "street.csv"
dataDir = "police_test"
dataDir=pathToDataDir + "/" + dataDir

for dirName in os.listdir(dataDir):
    subDirectory = os.path.join(dataDir + "/" + dirName)
    listOfFilesToMerge = filesToMerge(subDirectory, searchedType)
    mergeFiles(listOfFilesToMerge, targetDir + dirName + "-" + searchedType )

listOfFilesToMerge = filesToMerge(targetDir,searchedType)
mergeFiles(listOfFilesToMerge, targetDir + searchedType)
