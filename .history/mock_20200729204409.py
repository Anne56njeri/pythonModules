def isPowerOfTwo(n):
        # A number is a power of two if continously divided remainder is 0 
        if n == 1:
            return True
        elif n == 0 or n == 3:
            return False
        elif n < 0:
           
        while n > 1:
            print(n%2)
            if n % 2 != 0:
                return "false"
            n = n / 2 
        return "true"  

print(isPowerOfTwo(3))