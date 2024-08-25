#Write a function that returns the n-th number in the Fibonacci sequence.

def fibonacci(n):
    """Calculate a Fibonacci Series"""
    #initial variable for current fibonacci number
    #and previous fibonacci number
    result = 0
    before = 0
    for i in range(n):
        #first fibonacci number is 1
        #and since it does not have 'previous' number,
        #previous fibonacci number is still 0
        if i == 0:
            result = 1
        #other fibonacci number is the sum of
        #previous fibonacci number and previous of that number
        else:
            temp = before
            before = result
            result = before + temp

    return result

if __name__ == '__main__':
    print(fibonacci(5))  # Output: 5