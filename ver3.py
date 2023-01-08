import random
import sys
sys.setrecursionlimit(10**6)
def arrange(arr, low, high):
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