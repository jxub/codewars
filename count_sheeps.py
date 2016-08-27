def count_sheeps(arrayOfSheeps):
    sheeps = 0
    for i in range(len(arrayOfSheeps)):
        if arrayOfSheeps[i] == True:
            sheeps += 1
    return sheeps