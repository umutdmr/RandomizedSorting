
def recQuickSort(intArray, left, right):
    if right > left:
        median = medianOf3(intArray, left, right);
        partition = partitionIt(intArray, left, right, median);
        recQuickSort(intArray, left, partition - 1);
        recQuickSort(intArray, partition + 1, right);

  

def medianOf3(intArray, left, right):
    center = (left + right) // 2

    if (intArray[left] > intArray[center]):
        swap(intArray, left, center)

    if (intArray[left] > intArray[right]):
        swap(intArray, left, right)

    if (intArray[center] > intArray[right]):
        swap(intArray, center, right)

    swap(intArray, center, right - 1)
    return intArray[right - 1];

def swap(intArray, dex1, dex2):
    temp = intArray[dex1]
    intArray[dex1] = intArray[dex2]
    intArray[dex2] = temp

def partitionIt(intArray, left, right, pivot):
    leftPtr = left
    rightPtr = right - 1  
    while leftPtr <= rightPtr:
        print(6)
        while (intArray[leftPtr+1] < pivot):
            leftPtr += 1
        while (intArray[rightPtr-1] > pivot):
            rightPtr -= 1
        if (leftPtr >= rightPtr):
            break
        else:
            swap(intArray, leftPtr, rightPtr)

    swap(intArray, leftPtr, right - 1)
    return leftPtr

lst =[1,3,5,7,9,10,8,6,4,2]
low = 0
high = len(lst) - 1
print(lst)
recQuickSort(lst, low, high)
print(lst)