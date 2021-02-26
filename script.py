import os
import pandas as pd

pathToData="/media/frezer02/7D3CDB1B28552965/Data/bert/police"

listOfFilesToMerge=[]

for dirName in os.listdir(pathToData):
    subDirectory = os.path.join(pathToData,dirName)
    for fileName in os.listdir(subDirectory):
        if "street" in fileName: 
          pathToFile = os.path.join(subDirectory,fileName)
          listOfFilesToMerge.append(pathToFile)

combined_csv = pd.concat([pd.read_csv(f) for f in listOfFilesToMerge ])
combined_csv.to_csv( "/media/frezer02/7D3CDB1B28552965/Data/bert/street.csv", index=False, encoding='utf-8-sig')
