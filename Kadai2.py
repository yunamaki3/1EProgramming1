a, b = 0, 1
for i in range(50):
    print(b, end=' ')
    a, b = b, a+b
