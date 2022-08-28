# O n^3, we will simplify it by calling
# anything to the power of n as o^2

def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)

print_items(10)