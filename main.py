from ver1 import *
from ver2 import *
from ver3 import *
from ver4 import *
from input_creator import *
import time

all_n=[100, 1000, 10000]
version_number = 4

def execute_list_with_all_versions(lst):
    times=[]
    
    start_time = time.perf_counter() 
    quick_sort_version_1(lst,0,len(lst)-1)
    times.append((time.perf_counter()-start_time)*1e6)
    
    start_time = time.perf_counter() 
    quick_sort_version_2(lst,0,len(lst)-1)
    times.append((time.perf_counter()-start_time)*1e6)
    
    start_time = time.perf_counter() 
    quick_sort_version_3(lst,0,len(lst)-1)
    times.append((time.perf_counter()-start_time)*1e6)
    
    start_time = time.perf_counter() 
    quick_sort_version_4(lst,0,len(lst)-1)
    times.append((time.perf_counter()-start_time)*1e6)
    

    return times

def get_average_results(lists):
    list_times = []
    times = [0] * version_number
    for lst in lists:
        list_times.append(execute_list_with_all_versions(lst))
    for version in range(version_number):
        times[version] = sum([list_time[version] for list_time in list_times])
        times[version] /= len(list_times)
    return times

f = open("file.txt","w")

for n in all_n:
    f.write(f"***n= {n}\n\n")
    for int_type in range(1,5):
        f.write(f"InpType{int_type}\n")
        avarage_inputs = []
        for i in range(1,6):
            lst = create_input_with_type(n,int_type)
            f.write(f"Input{i} (average)= ")
            f.write("-".join(str(x) for x in lst))
            f.write("\n")
            avarage_inputs.append(lst)
        worst_input = create_input_with_type(n,int_type)
        worst_input = quick_sort_version_1(worst_input,0,len(worst_input)-1)
        f.write(f"Input (worst)=")
        f.write("-".join(str(x) for x in worst_input))
        f.write("\n\n")
        average_times = get_average_results(avarage_inputs)
        worst_times = execute_list_with_all_versions(worst_input)
        for version in range(1,version_number+1):
            f.write("Ver{} Average={:.2f} microseconds\n".format(version, average_times[version-1]))
            f.write("Ver{} Worst={:.2f} microseconds\n".format(version, worst_times[version-1]))
            
        f.write("\n")
    f.write("\n")
f.close()