# hackerrank problem: Birthday Cacke Candles


def birthdayCakeCandles(candles_list):
    # candles_list = sorted(candles_list)
    # print(candles_list)
    tallest_candle = 0
    big_candle = max(candles_list)

    for i in range(len(candles_list)):
        if candles_list[i] == big_candle:
            tallest_candle += 1

    return tallest_candle


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
