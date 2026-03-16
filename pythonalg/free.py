x = 1
def f():
    global x
    x += 1

f()
print(x)