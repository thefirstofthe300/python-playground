#! /usr/env/python

def main():
    fahrenheitTemps = [13.5, 19.6, 12.6, 8.5, 14.7, 6.2, 9.4, 18.2]
    celsiusTemps = [toFahrenheit(x) for x in fahrenheitTemps]
    
    for i in celsiusTemps: 
        print i
    
def toFahrenheit(celsiusTemp):
    return ((celsiusTemp * 1.8) + 32)
    
if __name__ == '__main__':
    main()