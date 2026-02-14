# Concentric Number Square
# Example (N = 4)

# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

n = 4

for i in range(1,n+1):
    for j in range(1,n+1):
        for j in range(1,n+1):
            if i == 1 or i == n or j == 1 or i == n:
                print(n)