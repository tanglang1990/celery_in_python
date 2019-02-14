import time


# def add(x, y):
#     time.sleep(4)
#     return x + y
from tasks import add

if __name__ == '__main__':
    print('start task...')
    r = add.delay(4, 8)
    print('end task...')
    print(r)


