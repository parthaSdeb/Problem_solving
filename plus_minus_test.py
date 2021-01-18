#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(test_array):
    positive_number_count = negative_number_count = zeros_count = 0
    array_length = len(test_array)

    for i in range(array_length):
        if arr[i] > 0:
            positive_number_count += 1
        elif arr[i] == 0:
            zeros_count += 1
        else:
            negative_number_count += 1

    positive_ratio = (positive_number_count / array_length)
    print(format(positive_ratio, '6f'))

    negative_ratio = (negative_number_count / array_length)
    print(format(negative_ratio, '6f'))

    zero_ratio = (zeros_count / array_length)
    print(format(zero_ratio, '6f'))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
