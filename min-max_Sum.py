# hackerrank problem: min max sum

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(test_array):
    total_sum = min_sum = max_sum = 0

    for i in range(len(test_array)):
        total_sum += test_array[i]

    # print("total sum: " + str(total_sum))

    test_array = sorted(test_array)
    # print(test_array)

    min_sum = (total_sum - max(test_array))
    max_sum = (total_sum - min(test_array))

    print(str(min_sum) + " " + str(max_sum))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
