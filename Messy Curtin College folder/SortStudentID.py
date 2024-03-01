import csv

def bubbleSort(ID):
    for testpass in range((len(ID)-1)-1):
        for ii in range(((len(ID)-1 - testpass)-1)):
            if ID[ii] > ID[ii+1]:
                temp = ID[ii]
                ID[ii] = ID[ii+1]
                ID[ii+1] = temp
    return ID

def insertionSort(ID):
    for nn in range(1, (len(ID)-1)):
        ii = nn
        temp = ID[ii]
        while ii > 0 and ID[ii-1] > temp:
            ID[ii] = ID[ii-1]
            ii-= 1
        ID[ii] = temp

    return ID

def selectionSort(ID):
    for nn in range((len(ID)-1)):
        minIdx = nn
        for ii in range(nn+1, len(ID)-1):
            if ID[ii] < ID[minIdx]:
                minIdx = ii
        temp = ID[minIdx]
        ID[minIdx] = ID[nn]
        ID[nn] = temp
    
    return ID

with open('RandomNames7000.csv') as studentID:
    dataFile = studentID.readlines()
    ID = []
    
    for line in dataFile:
        line = line.split(",")
        ID.append(line[0])

    ID = [int(i) for i in ID]

    choice = input("Please pick either [b]ubble sort, [i]nsertion sort or [s]election sort")
    
    choice = choice.lower()

    if choice == 'b':
        ID = bubbleSort(ID)
        with open('BubbleSortedIDs.csv', 'w') as sortedfile:
            for i in ID:
                sortedfile.write("%i\n" % i)


    elif choice == 'i':
        ID = insertionSort(ID)
        with open('InsertionSortedIDs.csv', 'w') as sortedfile:
            for i in ID:
                sortedfile.write("%i\n" % i)

    elif choice == 's':
        ID = selectionSort(ID)
        with open('SelectionSortedIDs.csv', 'w') as sortedfile:
            for i in ID:
                sortedfile.write("%i\n" % i)
    
    
   





