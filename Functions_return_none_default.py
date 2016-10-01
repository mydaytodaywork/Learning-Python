def hello():
    print("Hello")

print(hello())


def fibonacci(n):
    current, next = 0, 1

    for i in range(n):
        current, next = next, current + next

    return current
