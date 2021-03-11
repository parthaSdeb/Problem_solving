s = [1,2,1,3,2]
m = 2
d = 3


def birthday(s, d, m):
    sum = count = 0

    if m <= len(s):
        for i in range(m):
            sum += s[i]
            # print(sum)
    if sum == d:
        count +=1

    for i in range(len(s)-m):
        sum = sum - s[i] + s[i+m]
        if sum == d:
            count += 1

    return count


print(birthday(s, d, m))
