#! /usr/bin/python2

def main():
    sum = 0
    
    for x in range(0, 1000):
        if x % 3 == 0:
            print "Adding", x
            sum += x
        elif x % 5 == 0:
            print "Adding", x
            sum += x
    return sum

if __name__ == '__main__':
    print main()
