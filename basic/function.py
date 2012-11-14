import sys


def hello(name):
    print('Hello ' + name)
    print('Hello %s ' % name)

if __name__ == '__main__':
    hello(sys.argv[1])
