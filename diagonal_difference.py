#diagonal difference - Hackerrank
#https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=false


arr = [[1, 2, 3],
       [4, 5, 6],
       [9, 8, 9]]


def diagonalDifference(test_arr):
    left_diag = right_diag = result = 0
    array_length = len(test_arr)

    for i in range(array_length):
        left_diag += test_arr[i][i]
        right_diag += test_arr[i][array_length - 1 - i]

    result = abs(left_diag - right_diag)
    return result


solution = diagonalDifference(arr)
print(solution)


