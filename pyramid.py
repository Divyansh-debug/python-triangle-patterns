n = int(input("Give n : "))
for i in range(n):
    print(" " * (n-i-1) + "*" * (2*i + 1))