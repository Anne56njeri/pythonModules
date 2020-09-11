def isPowerOfTwo(self, n: int) -> bool:
        # A number is a power of two if continously divided remainder is 0 
        while n >= 0:
            if (n % 2) != 0:
                return "false"
            n = n / 2 
        return "true"  