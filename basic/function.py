import sys


def hello(name):
    print('Hello' % name)

if __name__ == '__main__':
    hello(sys.argv[1])
