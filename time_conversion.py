# hackerrank_problem -> time conversion

test_string = '12:45:54PM'

# print(test_string)


def timeConversion(s):
    # splitting the string and making a list
    splited_string = s.split(":")
    # print(splited_string)
    military_time = ""

    hour = int(splited_string[0])
    minute = splited_string[1]
    secPeriod = splited_string[2]
    sec = secPeriod[:2]
    # print(sec)
    period = secPeriod[2:]
    # print(period)

    if 0 <= hour < 12 and period == "AM":
        military_time = ((str(hour).zfill(2)) + ":" + minute + ":" + sec)
    elif 0 <= hour < 12 and period == "PM":
        military_time = (str(hour + 12) + ":" + minute + ":" + sec)
    elif hour == 12 and period == "AM":
        military_time = ("00" + ":" + minute + ":" + sec)
    elif hour == 12 and period == "PM":
        military_time = (str(hour) + ":" + minute + ":" + sec)
    return military_time


print(timeConversion(test_string))
