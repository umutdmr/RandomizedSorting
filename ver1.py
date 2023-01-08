#from input_creator import *
import sys
sys.setrecursionlimit(10**6)

def partition(lst, low, high):
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

def quick_sort_version_1(lst, low, high):
    if low < high:
        position = partition(lst, low, high)
        quick_sort_version_1(lst, low, position - 1)
        quick_sort_version_1(lst, position + 1, high)
    return lst