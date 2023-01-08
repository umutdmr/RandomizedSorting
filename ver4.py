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

"""lst =[1,3,5,7,9,10,8,6,4,2]
low = 0
high = len(lst) - 1
print(lst)
quick_sort_version_4(lst, low, high)
print(lst)"""

"""
import copy
class Version4():
    def median_of_three(self, arr, low, high):
        
        middle_index = (low+high) // 2
        first = arr[low]
        last = arr[high]
        middle = arr[middle_index]
        tmp_lst = copy.deepcopy([first, middle, last])
        for i in range(3):
            for j in range(3-i-1):
                if(tmp_lst[j] > tmp_lst[j+1]):
                   tmp_lst[j], tmp_lst[j+1] = tmp_lst[j+1], tmp_lst[j] 
        if tmp_lst[1] == first:
            return low, first
        elif tmp_lst[1] == last:
            return high, last
        
        return middle_index, middle
        
    def arrange(self, arr, low, high):
        right = low
        left = high 
        x = self.median_of_three(arr, low, high)[1]
        index_x = self.median_of_three(arr, low, high)[0]
        while right <= left:

            while right <= left and arr[right] <= x:
                right += 1
            while right <= left and arr[left] >= x:
                left -= 1

            if right < left:
                tmp = arr[right]
                arr[right] = arr[left]
                arr[left] = tmp


        arr[index_x] = arr[left]
        arr[left] = x
        return left
    
    def quick_sort(self, arr, low, high):
        if high > low:
            position = self.arrange(arr, low, high)
            self.quick_sort(arr, low, position - 1)
            self.quick_sort(arr, position + 1, high)

v = Version4()
lst =[1,3,5,7,9,10,8,6,4,2]
low = 0
high = len(lst) - 1
print(lst)
v.quick_sort(lst, low, high)
print(lst)
"""