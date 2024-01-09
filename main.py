#!/usr/bin/env python3

import utils
import sys
import re

from counter import countdown


def main():
    sounds = ["-s", "-s2", "-s3"]

    if (len(sys.argv) == 1) or sys.argv[1] == "-h":
        utils.display_help()

    elif sys.argv[1] in sounds:
        utils.play_sound(sys.argv[1])

    elif not re.search(r"\d", sys.argv[1]):
        print("Error! You have to adjust a valid time!")
        exit(1)

    elif sys.argv[1].isdigit():
        countdown(sys.argv[1])

    elif any(char.isalpha() and char.lower() not in ["h", "m", "s"] for char in sys.argv[1]):
        """
        Any other character than "h", "m" or "s" will result an error
        """
        print("Error! Incorrect time format")
        exit(2)

    else:
        countdown(sys.argv[1].lower())


if __name__ == "__main__":
    main()
