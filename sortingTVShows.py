def findIfTXT(fileName):
    reversefileName = fileName[::-1]
    splitFilename = reversefileName.split(".")
    if splitFilename[0] == 'txt':
        return fileName
    else:
        newfileName = fileName + '.txt'
        return newfileName


print('please enter file name:')
fileName = input()

filepath = str('C:\\Users\\torch\\Documents\\Virtual Studio Code\\Python Code\\') + findIfTXT(fileName)
print(filepath)

userFile = open(str(filepath))

outputList = userFile.readlines()

myDict = {}

showList = []

showListSplit = []

for index in range(len(outputList)):

    tempList = []
    listObject = outputList[index].strip('\n')
    if (index + 1 < len(outputList) and (index %2 == 0)):
        if int(listObject) in myDict:
            myDict[int(listObject)].append(outputList[index + 1].strip('\n'))
        else:
            tempList.append(outputList[index + 1]. strip('\n'))
            myDict[int(listObject)] =tempList
myDictSortedByKeys = dict(sorted(myDict.items()))


for x in myDict.keys():
    showList.append(myDict[x])


for x in showList:
    for i in x:
        showListSplit.append(i)


showListSplit = sorted(showListSplit)

f = open('outputKeys.txt', 'w')

for key, value in myDictSortedByKeys.items():
    f.write(str(key) + ": ")
    for item in value[:-1]:
        f.write(item + "; ")
    f.write(value[-1])
    f.write("\n")
f.close()

f = open('outputTitles.txt', 'w')
for item in showListSplit:
        f.write(item + '\n')
f.close()