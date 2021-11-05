def all_permutations(permList, nameList):
    size = len(nameList)

    if size == 0:
        for i in range(len(permList)):
            print(permList[i], end = ' ')
        print()
    else:
        for i in range(size):
            newPerms = permList.copy()
            newPerms.append(nameList[i])
            newNames = nameList.copy()
            newNames.pop(i)
            all_permutations(newPerms, newNames)

if __name__ == "__main__":
    nameList = 'Julia Lucas Mia'.split(' ')
    permList = []
    all_permutations(permList, nameList)