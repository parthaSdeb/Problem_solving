# Hackerrank problem: between two sets

a = [2, 4]
b = [16, 32, 96]


def getTotalX(a, b):
    multipliers_of_A = []
    factors_of_B = []
    final_integers = []
    total_length = len(a+b)

    for i in range(1, 101):
        for numbers_a in a:
            if i % numbers_a == 0:
                multipliers_of_A.append(i)

        for numbers_b in b:
            if numbers_b % i == 0:
                factors_of_B.append(i)

    numbers_list = multipliers_of_A + factors_of_B
    for number in numbers_list:
        if numbers_list.count(number) == total_length:
            final_integers.append(number)

    return len(set(final_integers))

    # print(multipliers_of_A)
    # print(factors_of_B)
    # print(numbers_list)
    # print(final_integers)
    # print(set(final_integers))


print(getTotalX(a, b))
