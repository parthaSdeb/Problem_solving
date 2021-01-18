# n = int(input('enter the range of the array: '))
# print(n)

# test_list= []
# for i in range(n):
#     x = int(input('enter number: '))
#     # print(x)
#     test_list.append(x)

# print(test_list)


# Complete the aVeryBigSum function below.
def aVeryBigSum(ar, ar_count):
    sum = 0
    for i in range(ar_count):
        sum = sum + int(ar[i])
    return sum
