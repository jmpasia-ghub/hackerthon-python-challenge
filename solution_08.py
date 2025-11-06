# Read input from STDIN. Print output to STDOUT

# obtain the size of the dictionary
n = int(input())

# define the dictionary variable
dictnry = {}

# save the input words into dictnry
for i in range(n):
    word = input().split()
    dictnry[word[0]] = word[1]
    
# return the phone numbers if present in the dictionary
while True:
    try:
        name = input()
        if name in dictnry:
            print(f"{name}={dictnry[name]}")
        else:
            print("Not found")
    except EOFError:
        break
        
