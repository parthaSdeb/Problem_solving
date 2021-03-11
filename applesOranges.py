# hackerank problem: Apples and Oranges

s = 7
t = 11
a = 5
b = 15
apples = [-2, 2, 1]
oranges = [5, -6]


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_test = []
    orange_test = []
    count_A = count_O = 0

    #   determining the actual position of apples
    for i in apples:
        apple_test.append(i + a)
    # print(apple_test)

    #   determining the actual position of oranges
    for j in oranges:
        orange_test.append(j + b)
    # print(orange_test)

# counting the amount of apples falls in sams house
    for x in apple_test:
        if s <= x <= t:
            count_A += 1

# counting the amount of oranges falls in sams house
    for y in orange_test:
        if s <= y <= t:
            count_O += 1

    print(count_A)
    print(count_O)


countApplesAndOranges(s, t, a, b, apples, oranges)
