def gen(n):
    i = 0
    while i < n:
        yield i
        i += 1

for x in gen(5):
    print(x)

def gen(n):
    i = 0
    while i < n:
        yield i
        i += 1

for x in gen(5):
    print(x)

def gen():
    for i in range(5):
        yield i * i

for x in gen():
    print(x)

def gen():
    yield "a"
    yield "b"
    yield "c"

for x in gen():
    print(x)

def gen(n):
    for i in range(1, n + 1):
        yield i * 2

for x in gen(4):
    print(x)

