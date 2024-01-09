#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(A):
    for testpass in range((len(A)-1)-1):
        for ii in range(((len(A)-1 - testpass)-1)):
            if A[ii] > A[ii+1]:
                temp = A[ii]
                A[ii] = A[ii+1]
                A[ii+1] = temp

def insertionSort(A):
    for nn in range(1, (len(A)-1)):
        ii = nn
        temp = A[ii]
        while ii > 0 and A[ii-1] > temp:
            A[ii] = A[ii-1]
            ii -= 1
            A[ii] = temp


def selectionSort(A):
    for nn in range((len(A)-1)):
        minidx = nn
    for ii in range(nn+1, len(A)-1):
        if A[jj]<A[minIdx]:
            minidx = ii
    temp = A[minidx]
    A[minidx] = A[nn]
    A[nn] = temp

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


