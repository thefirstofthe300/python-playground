#! /usr/bin/python2

def main():
    print smallest_evenly_divisible(0, 20)

def prime_factors(number):
    """ Finds the prime factors of a number
    
    Args:
        integer: number for which to find the factors
    Returns:
        A dict mapping the factor to the number of times it is used as a factor
    """
    factors = {}
    smallest_factor = 2

    if number == 0:
        return {}
    elif number == 1:
        return {}
    else:
        while number != 1:
            if number % smallest_factor == 0:
                if factors.get(smallest_factor) == None:
                    factors[smallest_factor] = 1
                else:
                    factors[smallest_factor] += 1
                number /= smallest_factor
            else:
                smallest_factor += 1

    return factors

def most_factors(first, second):
    """ Returns the factors of the lowest common multiple.
    
    Takes in a dict or factors and a number, compares the factors in the dict
    to the factors of the number and returns a dict with the factors for the 
    least common multiple.
    
    Args:
        first: dict of factors of the first number
        second: second number to compare factors
        
    Returns:
        most_factors: the factors of the lowest common multiple
    """
    first_factors = first
    second_factors = prime_factors(second)

    most_factors = {}

    for i in first_factors:
        if first_factors[i] > second_factors.get(i, 0):
            most_factors[i] = first_factors[i]
        else:
            most_factors[i] = second_factors.get(i, 0)

    for i in second_factors:
        if second_factors[i] > most_factors.get(i, 0):
            most_factors[i] = second_factors.get(i, 0)

    return most_factors

def smallest_evenly_divisible(begin, end):
    """ Retutns the smallest number evenly divisible by all numbers within a
    given range.
    
    Args:
        begin: start of range
        end: end of the range
    Returns:
        product: smallest evenly divisible number
    """
    factors = {}
    product = 1

    for i in range(begin, end):
        if i != 0 and i != 1:
            if i == 2:
                factors[i] = 1
            else:
                factors = most_factors(factors, i)
    for i in factors:
        product *= (i ** factors[i])

    return product

if __name__ == '__main__':
    main()
    