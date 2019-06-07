#!/bin/python3

import sys
from operator import itemgetter

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in range(n):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(arr_t)
    k = int(input().strip())
    arr1 = sorted(arr, key=itemgetter(k))
    for i in arr1:
        for j in i:
            print(j,end = ' ')
        print()    
