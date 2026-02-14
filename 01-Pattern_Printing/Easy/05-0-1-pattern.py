# Print alternating 0-1 pattern.

# 1
# 01
# 101
# 0101

n = 8
for i in range(0,n+1):
    num = int()
    if i % 2 == 1:
        num = 0
    else:
        num = 1
    for j in range(1,i+1):
        print(num % 2, end = '')
        num = num + 1
    print()

n = 7
for i in range(1,n+1):
    #calculate starting point
    num = int()
    if i % 2 == 1:
        num = 0
    else:
        num = 1
    for j in range(1, i+1):
        print(num, end ="")
        #alternate
        if num == 0:
            num = 1
        else:
            num = 0
    print()
    