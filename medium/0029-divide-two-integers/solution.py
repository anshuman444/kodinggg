class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        
        negative = (dividend < 0) ^ (divisor < 0)

        
        dvd = abs(dividend)
        dvs = abs(divisor)

        quotient = 0

        
        while dvd >= dvs:
            temp_divisor = dvs
            multiple = 1
            
            while dvd >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            dvd -= temp_divisor
            quotient += multiple

        if negative:
            quotient = -quotient

        
        return max(INT_MIN, min(INT_MAX, quotient))