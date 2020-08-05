import math 
class Solution: 
    def divide(self, dividend: int, divisor: int) -> int:
        answer = math.trunc(dividend / divisor)
        if answer > (pow(2, 31) - 1):
            answer = pow(2, 31) - 1 
        elif answer < (pow(2, 31) * (-1)): 
            answer = pow(2, 31) * (-1) 
        return answer