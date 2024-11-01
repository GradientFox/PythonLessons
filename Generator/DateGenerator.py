from calendar import weekday
from datetime import date, timedelta


def generate_dates(year, month, day):
    i = 0
    while True:
        yield str(date(year,month,day) + timedelta(days=i))
        i += 1


def generate_dow(year, month, day):
    i = 0
    while True:
        match (date(year,month,day) + timedelta(days=i)).weekday():
            case 0:
                yield "Понедельник"
            case 1:
                yield "Вторник"
            case 2:
                yield "Среда"
            case 3:
                yield "Четверг"
            case 4:
                yield "Пятница"
            case 5:
                yield "Суббота"
            case 6:
                yield "Воскресенье"
        i += 1


def make_tuple_day(year, month, day):
    d = generate_dates(year, month, day)
    w = generate_dow(year, month, day)
    yield tuple([next(d), next(w)])

x = make_tuple_day(2024, 10, 22)
for i in range(30):
    print(next(x))

