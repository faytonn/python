import sys
from hmac import new
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        d = gcd(numerator, denominator)
        
        numerator //= d
        denominator //= d
        
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
            
        self.numerator = numerator
        self.denominator = denominator
    

    def __repr__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"
    
    def add(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        
        return Fraction(new_num, new_den)
    
    def sub(self, other):
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)
    
    def mul(self, other):
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)
    
    def div(self, other):
        if other.numerator == 0:
            return None
        new_num = self.numerator * other.denominator 
        new_den = self.denominator * other.numerator
        
        return Fraction(new_num, new_den)
    
def parse_fraction(s):
    s = s.strip()
    if '/' in s:
        parts = s.split('/')
        num = int(parts[0])
        den = int(parts[1])
        return Fraction(num, den)
    else:
        num = int(s)
        return Fraction(num, 1)
    
def evaluate_expression(line):
    line = line.strip()
    operators = ['+', '-', '*', '\\']
    op = None
    
    for oper in operators:
        if oper in line:
            op = oper
            break
    
    if op is None:
        return 'invalid'
    
    left, right = line.split(op, 1)
    
    frac1 = parse_fraction(left)
    frac2 = parse_fraction(right)
    
    if op == '+':
        result = frac1.add(frac2)
    elif op == '-':
        result = frac1.sub(frac2)
    elif op == '*':
        result = frac1.mul(frac2)
    elif op == '\\':
        result = frac1.div(frac2)
        
    if result is None:
        return 'invalid'
    else:
        return str(result)
    
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        print(evaluate_expression(line))