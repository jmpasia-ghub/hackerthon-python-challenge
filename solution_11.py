import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = float('-inf')
    for i in range(4):
        
        for j in range(4): 
            
            # get a 3x3 submatrix (without numpy)
            A = [row[j:3+j] for row in arr[i:3+i]]
            # get the sum of the matrix
            sum_A = sum(sum(a) for a in A)
            # subtract the 1st and 3rd elements of the 2nd row
            sum_A = sum_A - A[1][0] - A[1][2]
            # update the maximum sum
            max_sum = max(sum_A, max_sum)
            
    print(max_sum)
            
