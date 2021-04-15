from time import time
from time import sleep


def duration(function):
    def wrapper(*args, **kwargs):
        print(args),
        print(kwargs)
        start = time()
        output = function(*args, **kwargs)
        stop = time()
        print(f'Function time {stop - start}')
        return output

    return wrapper


@duration
def timer(time):
    sleep(time)
    print('I want to sleep.')
    sleep(time)


timer(3)

