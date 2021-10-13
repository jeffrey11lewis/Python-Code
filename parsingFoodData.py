column1 = []
column2 = []
column3 = []
column4 = []

#print('input file name:')
inputFileName = "C:\\Users\\torch\Documents\\Virtual Studio Code\\Python Code\\food.txt"
#inputFileName = input()
f = open(inputFileName)

for row in f:
    fields = row[:-1].split('\t')
    column1.append(fields[0])
    column2.append(fields[1])
    column3.append(fields[2])
    column4.append(fields[3])

for rowNum in range(len(column4)):
    if column4[rowNum] == "Available":
        print(column4[rowNum] + " (" + column1[rowNum] + ") -- " + column3[rowNum])