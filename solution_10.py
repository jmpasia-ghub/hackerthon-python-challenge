#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    rem = []
    # quotient and remainder when a number is divided by 2
    def divide_by_two(m):
        return m//2, m%2
    
    ###############################################
    # create own's converter from base 10 to base 2 
    ###############################################
    while n >= 2:
        try: 
            q, r = divide_by_two(n)
            rem.append(r)
            n = q
        except:
            print("Something is wrong")
            break
    # add the last coefficient
    rem.append(1)
    ###############################################
    
    # reverse and save as string
    rem = "".join(str(x) for x in rem[::-1])
    
    ###############################################
    # find the maximum consecutive
    ###############################################
    count = 0
    max_count = 0
    
    for char in rem:
        if char == '1':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    
    print(max_count) 
