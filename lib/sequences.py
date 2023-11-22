#!/usr/bin/env python3

def print_fibonacci(length):
    my_list =[]

    if length >= 1:
        my_list.append(0)
    if length >= 2:
        my_list.append(1)
    for n in range(2,length):
        next_number = my_list[-1] + my_list[-2]
        my_list.append(next_number)
        
    print(my_list)
print_fibonacci(9)