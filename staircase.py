# hackerrank -> problem 3: staircase problem


def staircase(n):
    for i in range(n):
        # for loop to print required space (n-i-1)
        for s in range(n - i - 1):
            print(' ', end='')
        # for loop to print required # (i+1)
        for j in range(i + 1):
            print('#', end='')
        print()


staircase(5)

# def staircase(n):
#     for i in range(n):
#         # for loop to print required space (n-i-1)
#         for s in range(n - i - 1):
#             print(' ', end='')
#         # for loop to print required # (i+1)
#         for j in range(i + 1):
#             print('#', end='')
#         print()
#
#
# if __name__ == '__main__':
#     n = int(input())
#
#     staircase(n)
