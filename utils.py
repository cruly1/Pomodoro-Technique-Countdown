import os


def display_help():
    print("--- Pomodoro Countdown ---\n")
    print("Usage:\n")
    print("{:<20} {:>5}".format("-h", "Display Help"))
    print("{:<20} {:>5}".format("-s, s2, s3", "Play sound once, twice or three times"))
    print("{:<20} {:>5}".format("<time>", "Adjust time in different formats:"))
    print("{:>23} {:>16}".format("60", "-> 60 seconds"))
    print("{:>24} {:>15}".format("60s", "-> 60 seconds"))
    print("{:>23} {:>14}".format("1m", "-> 1 minute"))
    print("{:>26} {:>14}".format("1m15s", "-> 1 minute 15 seconds"))
    print("{:>26} {:>14}".format("1m15s", "-> 1 minute 15 seconds"))
    print("{:>25} {:>20}".format("1h5m", "-> 1 hour 5 minutes"))


def play_sound(arg):
    li = [e for e in [*arg] if e.isnumeric()]
    if not li:
        times = 1
    else:
        times = int("".join(li))

    for i in range(times):
        _sound = "chipichapa.mp3"
        print(f"Now playing {_sound}")
        os.system(f"afplay {_sound}")
