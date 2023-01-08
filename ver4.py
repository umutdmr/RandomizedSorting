import copy
import sys
sys.setrecursionlimit(10**6)

def median_of_three(arr, low, high):
    middle_index = (low+high) // 2
    first = arr[low]
    last = arr[high]
    middle = arr[middle_index]
    tmp_lst = copy.deepcopy([first, middle, last])
    for i in range(3):
        for j in range(3-i-1):
            if(tmp_lst[j] > tmp_lst[j+1]):
               tmp_lst[j], tmp_lst[j+1] = tmp_lst[j+1], tmp_lst[j] 
    if tmp_lst[1] == last:
        arr[low], arr[high] = arr[high], arr[low]
    elif tmp_lst[1] == middle:
        arr[low], arr[middle_index] = arr[middle_index], arr[low]
    
def arrange(arr, low, high):
    median_of_three(arr, low, high)
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
def quick_sort_version_4(arr, low, high):
    if high > low:
        position = arrange(arr, low, high)
        quick_sort_version_4(arr, low, position - 1)
        quick_sort_version_4(arr, position + 1, high)