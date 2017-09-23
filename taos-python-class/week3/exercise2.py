#! /usr/env/python

def main():
    originals = [74.3, -96.2, 75.5, -65.4, -75.3, -63.9, 95.2, 36.8, 74.0, 52.9, -94.3, 93]
    positives = [int(round(x)) for x in originals if x >= 0]
    
    for i in positives:
        print i
    
if __name__ == '__main__':
    main()