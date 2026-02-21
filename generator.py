def numbers():
    for i in range(3):
        yield i

print(list(numbers()))

def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(list(countdown(5)))

def letters():
    s = "abc"
    for ch in s:
        yield ch

print(list(letters()))

def even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

print(list(even(10)))

def squares(n):
    for i in range(n):
        yield i ** 2

g = squares(4)
print(next(g))
print(next(g))

