# hackerrank problem: Breaking the record

scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]


def breakingRecords(scores):
    min_score = max_score = 0
    min_count = max_count = 0

    for i in range(len(scores)):
        if i == 0:
            min_score = scores[i]
            max_score = scores[i]
        if i > 0:
            if scores[i] < min_score:
                min_score = scores[i]
                min_count += 1
            if scores[i] > max_score:
                max_score = scores[i]
                max_count += 1

    return [max_count, min_count]


result = breakingRecords(scores)
print(result)
