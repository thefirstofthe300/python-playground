#! /usr/bin/python2

def main():
    print largest_palindrome_product_in_range()

def is_palindrome(number):
    num_string = str(number)
    reverse_num_string = num_string[::-1]
    if num_string == reverse_num_string:
        return True
    return False

def largest_palindrome_product_in_range(minimum=100, maximum=999):
    largest_palindrome = 0 

    for i in range(minimum, maximum):
        for j in range(i, maximum):
            prod = j * i
            print prod
            if prod > largest_palindrome:
                if is_palindrome(prod):
                    largest_palindrome = prod

    return largest_palindrome

if __name__ == '__main__':
    main()