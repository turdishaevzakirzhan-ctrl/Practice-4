g = (i for i in range(5))
for x in g:
    print(x)

g = (i * 2 for i in range(5))
print(list(g))

g = (i * i for i in range(6))
print(list(g))

g = (i for i in range(10) if i % 2 == 1)
print(list(g))

nums = [1, 2, 3, 4]
g = (x + 1 for x in nums)
print(list(g))

