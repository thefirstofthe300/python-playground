#	Fibonacci	numbers	module		
def	fib(n):	#	write	Fibonacci	series	up	to	n		
    a, b = 0, 1		
    while b < n:		
        print b,		
        a, b = b, a+b

def	fib2(n):	#	return	Fibonacci	series	up	to	n		
    result = []		
    a, b = 0, 1		
    while b < n:		
        result.append(b)		
        a,b = b, a+b		
        return result		

def	test():	
    fib(1000)	
    fib2(100)	

if __name__ == '__main__':	
    test()