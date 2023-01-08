import random
import sys
sys.setrecursionlimit(10**6)
"""def arrange(arr, low, high):
    right = low
    left = high 
    x = arr[low]
    while right <= left:
        
        while right <= left and arr[right] <= x:
            right += 1
        while right <= left and arr[left] >= x:
            left -= 1

        if right < left:
            tmp = arr[right]
            arr[right] = arr[left]
            arr[left] = tmp

    
    arr[low] = arr[left]
    arr[left] = x
    return left



def quick_sort(arr, low, high):
    if high > low:
        position = arrange(arr, low, high)
        quick_sort(arr, low, position - 1)
        quick_sort(arr, position + 1, high)"""


"""lst =[1,3,5,7,9,10,8,6,4,2]
low = 0
high = len(lst) - 1
print(lst)
random.shuffle(lst)
quick_sort(lst, low, high)
print(lst)
"""

def arrange(arr, low, high):
    #random.shuffle(arr[low:high])
    right = low
    left = high 
    x = arr[low]
    while right <= left:
        while right <= left and arr[right] <= x:
            right += 1
        while right <= left and arr[left] >= x:
            left -= 1
        if right < left:
            tmp = arr[right]
            arr[right] = arr[left]
            arr[left] = tmp
    arr[low] = arr[left]
    arr[left] = x
    return left
def quick_sort(arr, low, high):
    if high > low:
        position = arrange(arr, low, high)
        quick_sort(arr, low, position - 1)
        quick_sort(arr, position + 1, high)
        
def quick_sort_version_3(arr, low, high):
    random.shuffle(arr)
    quick_sort(arr, low, high)
    
"""lst =[1,3,5,7,9,10,8,6,4,2]
low = 0
high = len(lst) - 1
print(lst)
quick_sort_version_3(lst, low, high)
print(lst)"""