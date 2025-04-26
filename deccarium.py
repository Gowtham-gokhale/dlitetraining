def g(a):
    b = str(a)
    c = 0
    for d in range(len(b)):
        c += int(b[d]) ** (d + 1)
    return c == a

print("1. Find first n Disarium numbers")
print("2. Find Disarium numbers between two numbers")

e = int(input("Enter choice (1 or 2): "))

if e == 1:
    h = int(input("Enter how many Disarium numbers to find: "))
    i = 0
    j = 0
    while i < h:
        if g(j):
            print(j, end=" ")
            i += 1
        j += 1

elif e == 2:
    k = int(input("Enter starting number: "))
    l = int(input("Enter ending number: "))
    for m in range(k, l + 1):
        if g(m):
            print(m, end=" ")

else:
    print("Invalid choice!")