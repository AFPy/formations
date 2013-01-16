import sys
print "test"
print __name__

def print_hello():
    print "hello world"

if __name__ == "__main__":
    print sys.argv[1]
    print sys.argv
