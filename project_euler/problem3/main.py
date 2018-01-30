#! /usr/bin/python2

from math import sqrt

def main():
    print factor(600851475143)

def factor(number):
    current_small_factor = 2
    current_large_factor = number
    search_cap = sqrt(number)
    while current_small_factor < search_cap:
        if current_large_factor % current_small_factor == 0:
            if current_large_factor == current_small_factor and current_large_factor != number:
                return current_large_factor
            current_large_factor /= current_small_factor
        else:
            current_small_factor += 1
    return current_large_factor

if __name__ == '__main__':
    main()