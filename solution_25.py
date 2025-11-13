def ceil(x):
    return(int(-1*(-x//1))) 

T = int(input())           # number of integers to test for primality
for i in range(T):
    n = int(input())
    if n == 1:
        print("Not prime")
    elif n == 2:
        print("Prime")        
    elif n%2 == 0:
        print("Not prime") 
    else:
        is_prime = True
        upper_lim = int(ceil(n)**0.5)+1
        for j in range(3, upper_lim, 2):
            if n%j == 0:
                is_prime = False
                break
        print("Prime" if is_prime else "Not prime")
        
