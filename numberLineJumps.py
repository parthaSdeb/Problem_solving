# Hackerrank problem: Number Line Jumps

x1 = 0
v1 = 2
x2 = 5
v2 = 3


def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return 'NO'
    elif v1 != v2 and (x2 - x1) % (v2 - v1) == 0:
        return 'YES'
    else:
        return 'NO'


result = kangaroo(x1, v1, x2, v2)
print(result)
