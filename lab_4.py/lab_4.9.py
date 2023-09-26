from datetime import datetime as dt
from datetime import timedelta as td


def week(weekday):
    weekdays = {1: "Понедельник",
               2: "Вторник",
               3: "Среда",
               4: "Четверг",
               5: "Пятница",
               6: "Суббота",
               7: "Воскресенье",
    }
    return weekdays.get(weekday)


def dat():
    print(
        f"сегодня {dt.now().date()}.\n"
        f"день недели - {week(dt.now().isoweekday())}"
    )
    n = int(input("введите количество дней"))
    today = dt.now()
    res = today + td(days=n)
    print(
        f"через {n} дней будет {res.date()}\n"
        f"день недели - {week(res.isoweekday())}"
    )


dat()
