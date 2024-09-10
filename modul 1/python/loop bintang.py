# n = 6
# for k in range(n):
#     i = 5
#     j = 0
#     print(''*i+'*'*(j+k))


n = 10
# for i in range(n):
#         print(' '*(n-i-1)+'*'*(2*i+1))
    

# for i in range(n-2,-1,-1):
#     print(' '*(n-i-1)+'*'*(2*i+1))


n = 4  
rows = 2*n-1

for i in range(rows):
    if i<n:
        space = n - i - 1
        star = 2 * i + 1
    else:
        space = i - n + 1
        star = 2 * (rows - i - 1) + 1
    
    print(' '*space+'*'*star)