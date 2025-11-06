#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    L = len(a)
    no_of_swaps = 0
    tot_swaps = 0
    
    def swap(x, y):
        if x > y:
            return(y,x, True)
        else:
            return(x, y, False)
            
    
    for i in range(L):
        no_of_swaps = 0
        for j in range(L-1):
            a[j], a[j+1], isSwap = swap(a[j], a[j+1])
            if isSwap:                
                no_of_swaps += 1
                tot_swaps += 1
        if no_of_swaps == 0: break
    
    print(f"Array is sorted in {tot_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")
