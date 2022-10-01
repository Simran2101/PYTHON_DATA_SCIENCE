x = []
for i in range(10):
    n = input('enter value::')
    x.append(n)

print("the values entered were")
x.sort()
for val in x:
    print(val, end=' ')
# print(' '.join(x))
