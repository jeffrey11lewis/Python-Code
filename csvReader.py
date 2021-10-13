import csv
print('please input the name of the csv file you are looking for:')


def findIfCSV(fileName):
    #print('hello from findIfCSV')
    reversefileName = fileName[::-1]
    #print(reversefileName)
    splitFilename = reversefileName.split(".")

    #print(splitFilename[0])

    if splitFilename[0] == 'vsc':
        #print('yay! no problem.')
        return fileName
        
    else:
        newfileName = fileName + '.csv'
        #print('the new filename is ' + newfileName)
        return newfileName




fileName = input()

#findIfCSV(fileName)

filepath = str('C:\\Users\\torch\\Documents\\Virtual Studio Code\\Python Code\\') + findIfCSV(fileName)



print(filepath + ' is the filepath')
print(findIfCSV(fileName) + ' is the filename\n')

wordList = []

with open (str(filepath), 'r') as csvfile:
    userFile = csv.reader(csvfile, delimiter = ',')

    for row in userFile:
        for index in range(len(row)):
            if row[index] not in wordList:
                print('{} {}'.format(row[index], row.count(row[index])))
                wordList.append(row[index])