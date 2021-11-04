# create decorators with decorators function

def fib(number):
    a, b = 0, 1

    while a < number:
        yield a
        a, b = b, a + b


x = fib(10)
print(type(x), x)
print(f"next fibonacci: {x.__next__()}")
print(f"next fibonacci: {x.__next__()}")
print(f"next fibonacci: {x.__next__()}")
print(f"next fibonacci: {x.__next__()}")
print(f"next fibonacci: {x.__next__()}")

# print("\n Using for in loop")
# for i in fib(10):
#     print(type(i), i)
