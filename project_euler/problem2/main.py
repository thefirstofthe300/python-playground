#! /usr/bin/python2

import unittest

fib_nums = []

def main():
    print forward_fibonacci(10)
    print sum_even(forward_fibonacci(10))
    test_sum_even()
    test_forward_fibonacci()
    
def forward_fibonacci(cap):
    fib_ints = []
    current_num = 0

    if cap < 0:
        raise ValueError("Yo dawg, cap has to be positive.")
    
    while current_num < cap:

        # Start bootstrapping the sequence
        if current_num == 0:
            fib_ints.append(current_num)
            current_num = 1
        # If the sequence still hasn't been fully bootstrapped
        elif len(fib_ints) == 1:
            # Finish bootstrapping
            fib_ints.append(1)
        else:
            
            # Terminate the loop if the next number in the sequence will be greater than the user specified cap
            if current_num > cap:
                return fib_ints

            # At this point, the sequence is fully bootstrapped
            fib_ints.append(current_num)
            current_num = fib_ints[-1] + fib_ints[-2]

    return fib_ints

def sum_even(int_array):
    sum = 0

    for i in int_array:
        if i % 2:
            sum += i
    
    return sum

def test_sum_even():
    int_array = [2, 4, 6, 3, 5, 6]
    assert sum_even(int_array) == 18

def test_forward_fibonacci():
    cap1 = 10
    cap2 = 0
    cap3 = 1
    cap4 = 2
    cap5 = -1

    assert forward_fibonacci(cap1) == [0, 1, 1, 2, 3, 5, 8]
    assert forward_fibonacci(cap2) == []
    assert forward_fibonacci(cap3) == [0]
    assert forward_fibonacci(cap4) == [0, 1, 1]
    try:
        assert forward_fibonacci(cap5)
    except ValueError as e:
        print "It errored out, yo."

if __name__ == '__main__':
    main()
