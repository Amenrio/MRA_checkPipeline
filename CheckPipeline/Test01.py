a = [1,2,2,3,4]

def even(x):
    return x % 2 == 0



for item in a[:]:
    if even(item):
        a.remove(item)

print(a)