# Enter your code here. Read input from STDIN. Print output to STDOUT

d_ret = list(map(int, input().split()))
d_due = list(map(int, input().split()))

d_ret_day, d_ret_mon, d_ret_yea = d_ret
d_due_day, d_due_mon, d_due_yea = d_due

if d_ret_yea > d_due_yea:
    fine = 10000
elif d_ret_mon > d_due_mon and d_ret_yea == d_due_yea:
    fine = 500*(d_ret_mon - d_due_mon)
elif d_ret_day > d_due_day and d_ret_mon == d_due_mon and d_ret_yea == d_due_yea:
    fine = 15*(d_ret_day - d_due_day)
else:
    fine = 0
print(fine)   
