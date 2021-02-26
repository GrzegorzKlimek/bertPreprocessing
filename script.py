import os
import pandas as pd

pathToDataDir="/media/frezer02/7D3CDB1B28552965/Data/bert/"
searchedType="street.csv"
dataDir="police_test"
listOfFilesToMerge=[]
dataDir=pathToDataDir + "/" + dataDir
combined_csv_file_path = pathToDataDir + "/" + searchedType

for dirName in os.listdir(dataDir):
    subDirectory = os.path.join(dataDir + "/" + dirName)
    for fileName in os.listdir(subDirectory):
        if searchedType in fileName:
            pathToFile = os.path.join(subDirectory,fileName)
            listOfFilesToMerge.append(pathToFile)

combined_csv = pd.concat([pd.read_csv(f) for f in listOfFilesToMerge ])
combined_csv.to_csv( combined_csv_file_path, index=False, encoding='utf-8-sig')
