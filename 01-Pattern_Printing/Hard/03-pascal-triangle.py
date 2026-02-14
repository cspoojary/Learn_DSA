# Example (N = 5)

#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   6   4   1

n=5
num = 1
for i in range(1,n+1):
    for j in range(1, n-i+1):
        print(" ", end="")
    for j in range(1,i+1):
            print(num,  end=" ")
    print()