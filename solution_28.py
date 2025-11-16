#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())

    list_email = []
    list_name = []
    
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        list_name.append(firstName)
        list_email.append(emailID)
        

    def get_names(firstName, emailID):
        pattern = re.compile(r'@gmail\.com$', re.IGNORECASE)  
        idx = [i for i, email in enumerate(emailID) if pattern.search(email)]
        names = [firstName[i] for i in idx]
        return names
        
    names = get_names(list_name, list_email)
    for nm in sorted(names):
        print(nm)
        
    
    
