import random
from input_creator import *

def select_random_pivot(lst, low, high):
    pivot_index = random.randint(low, high)
    lst[low], lst[pivot_index] = lst[pivot_index], lst[low]

def partition_with_random_pivot(lst, low, high):
    select_random_pivot(lst, low, high)
    pivot = lst[low]
    k = high
    i = high
    while(i > low):
        if lst[i] > pivot:
            lst[k], lst[i] = lst[i], lst[k]
            k-=1
        i-=1
    lst[k], lst[low] = lst[low], lst[k]
    return k



def quick_sort_version_2(lst, low, high):
    if low < high:
        position = partition_with_random_pivot(lst, low, high)
        quick_sort_version_2(lst, low, position - 1)
        quick_sort_version_2(lst, position + 1, high)
    return lst

lst = create_input_with_type(n=20,int_type=2)
print(quick_sort_version_2(lst,0,len(lst)-1))