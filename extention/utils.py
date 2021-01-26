from . import jalali
from django.utils import timezone

def PersianNumConverter(mystr):
    nubers ={
        "0" : "۰",
        "1" : "۱",
        "2" : "۲",
        "3" : "۳",
        "4" : "۴",
        "5" : "۵",
        "6" : "۶",
        "7" : "۷",
        "8" : "۸",
        "9" : "۹",

    }

    for e, p in nubers.items():
        mystr = mystr.replace(e, p)

    return mystr

def JalaliDjango(time):
    JMonth = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند"
    ]

    time = timezone.localtime(time)

    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    TimeToTuple = jalali.Gregorian(time_to_str).persian_tuple()

    TimeToList = list(TimeToTuple)

    for index, month in enumerate(JMonth):
        if TimeToList[1] == index + 1:
            TimeToList[1] = month
            break

    output = "{} {} {} ، ساعت {}:{}".format(
        TimeToList[2],
        TimeToList[1],
        TimeToList[0],
        time.hour,
        time.minute,
    )

    return PersianNumConverter(output)


