import os

pathToData="/media/frezer02/7D3CDB1B28552965/Data/bert/"

for dirName in os.listdir(pathToData):
    subDirectory = os.path.join(pathToData,dirName)
    # print(subDirectory)
    for fileName in os.listdir(subDirectory):
      print(fileName)

