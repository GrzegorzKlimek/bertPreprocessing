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
    if len(listOfFiles) < 1:
        return
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
targetDir = pathToDataDir + "output/police/"
searchedType = "street.csv"
dataDir = "police"
dataDir=pathToDataDir + "/" + dataDir

# merge files by month
for dirName in os.listdir(dataDir):
    subDirectory = os.path.join(dataDir + "/" + dirName)
    listOfFilesToMerge = filesToMerge(subDirectory, searchedType)
    mergeFiles(listOfFilesToMerge, targetDir + "months/" + dirName + "-" + searchedType )
    
# # merge files by year
for year in range(2010, 2021):
    listOfFilesToMerge = filesToMerge(targetDir + "months/",str(year))
    mergeFiles(listOfFilesToMerge, targetDir + "years/" + str(year) + "-" + searchedType)
#
# # merge files all files
listOfFilesToMerge = filesToMerge(targetDir + "years/",searchedType)
mergeFiles(listOfFilesToMerge, targetDir + searchedType)
