def gen_secs():
    for sec in range(60):
        yield sec


def gen_minutes():
    for minute in range(60):
        yield minute


def gen_hours():
    for hour in range(24):
        yield hour


def gen_time():
    gn_hr = gen_hours()
    while 1:
        try:
            hour = next(gn_hr)
        except StopIteration:
            break
        else:
            gn_min = gen_minutes()
        while 1:
            try:
                minute = next(gn_min)
            except StopIteration:
                break
            else:
                gn_sec = gen_secs()
            while 1:
                try:
                    second = next(gn_sec)
                except StopIteration:
                    break
                else:
                    yield "%02d:%02d:%02d" % (hour, minute, second)


def gen_years(start_year=2020):
    while True:
        yield start_year
        start_year += 1


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    dict_months_and_days = {31: [1, 3, 5, 7, 8, 10, 12], 30: [4, 6, 9, 11], 29 - leap_year: [], 28 + leap_year: [2]}
    # When leap year in Feb there is 29 days, otherwise, 28 days.

    for num_of_days in dict_months_and_days:
        if month in dict_months_and_days[num_of_days]:
            for day in range(1, num_of_days + 1):
                yield day


def gen_date():
    gn_yr = gen_years()
    while 1:
        try:
            year = next(gn_yr)
        except StopIteration:
            break
        else:
            leap_year = year % 4 == 0
            gn_mon = gen_months()
        while 1:
            try:
                month = next(gn_mon)
            except StopIteration:
                break
            else:
                gn_day = gen_days(month, leap_year)
            while 1:
                try:
                    day = next(gn_day)
                except StopIteration:
                    break
                else:
                    gn_time = gen_time()
                while 1:
                    try:
                        time = next(gn_time)
                    except StopIteration:
                        break
                    else:
                        yield "%02d/%02d/%04d %s" % (day, month, year, time)


# ---- 4 -----
# for gt in gen_time():
#     print(gt)

# ----- 8 ------
i = 0
for gd in gen_date():
    i += 1
    if i < 10000000:
        print(gd)
    else:
        break

# ----- 9 -------
i = 0
for gd in gen_date():
    i += 1
    if i % 1000000 == 0:
        print(gd)


