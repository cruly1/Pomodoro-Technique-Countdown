import datetime
import os
import time

from utils import play_sound

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE


def get_seconds(arg) -> int:
    if arg.isnumeric():
        return int(arg)

    result = 0
    clock = {}

    val = ""
    for c in arg:
        if c.isnumeric():
            val += c
        else:
            if val:
                clock[c] = int(val)
                val = ""

    for time_unit in clock.keys():
        if time_unit == "h":
            result += clock[time_unit] * HOUR
        elif time_unit == "m":
            result += clock[time_unit] * MINUTE
        else:
            result += clock[time_unit] * SECOND

    return result


def countdown(arg: str) -> None:
    result = get_seconds(arg)
    tmp = result

    for i in range(result+1, 1, -1):
        os.system("clear")
        print(str(datetime.timedelta(seconds=tmp)))
        time.sleep(1)
        tmp -= 1

    os.system("clear")
    play_sound("s")
