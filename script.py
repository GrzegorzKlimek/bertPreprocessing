import os
import pandas as pd

pathToDataDir="/media/frezer02/7D3CDB1B28552965/Data/bert/"
searchedType="street.csv"
dataDir="police"
listOfFilesToMerge=[]
dataDir=pathToDataDir + "/" + dataDir
combined_csv_file_path = pathToDataDir + "/" + searchedType

for dirName in os.listdir(dataDir):
    subDirectory = os.path.join(dataDir + "/" + dirName)
    for fileName in os.listdir(subDirectory):
        if searchedType in fileName:
            pathToFile = os.path.join(subDirectory,fileName)
            listOfFilesToMerge.append(pathToFile)
print("found list of files to merge")
combined_csv = pd.read_csv(listOfFilesToMerge[0])
del listOfFilesToMerge[0]
for f in listOfFilesToMerge:
    print("processing file: " + f)
    try:
        combined_csv = pd.concat([pd.read_csv(f), combined_csv ])
    except Exception:
        print("for file " + f + " there was exception: " + str(Exception))

combined_csv.to_csv( combined_csv_file_path, index=False, encoding='utf-8-sig')
