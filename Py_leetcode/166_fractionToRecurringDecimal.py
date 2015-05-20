import sys
import math

"""
    Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

    If the fractional part is repeating, enclose the repeating part in parentheses.

    For example,

    Given numerator = 1, denominator = 2, return "0.5".
    Given numerator = 2, denominator = 1, return "2".
    Given numerator = 2, denominator = 3, return "0.(6)".
"""
def fraction_to_decimal(numerator, denominator):
    n = numerator
    d = denominator

    sign = '-' if n * d < 0 else ''
    n = abs(n)
    d = abs(d)

    res = []
    res.append(sign)
    res.append(str(n / d))
    rem = n % d
    if not rem:
        return ''.join(res)
    
    res.append('.')
    seen = {}
    while not rem in seen:
        seen[rem] = len(res)
        res.append(str(10 * rem / d))
        rem = 10 * rem % d

    idx = seen[rem]
    res.insert(idx, '(')
    res.append(')')
    return ''.join(res).replace('(0)', '')

#print fraction_to_decimal(1, 2)
#print fraction_to_decimal(2, 3)
print fraction_to_decimal(1, 19)


def fractionToDecimal(self, numerator, denominator):
    n = numerator
    d = denominator
    if n % d == 0:
        return str(n//d)

    # Deal with negatives
    if (abs(n)/n) * (abs(d)/d) < 0:
        res = '-'
        n = abs(n)
        d = abs(d)
    else:
        res = ''

    # Integer part
    res = res + str(n//d) + '.'
    n = n % d

    # Start point of the "list"
    frem = n
    srem = n
    firstTime = True
    while frem != 0 and not (firstTime == False and frem == srem):
        firstTime = False
        srem = (srem * 10) % d
        frem = (frem * 10) % d
        if frem:
            frem = (frem * 10) % d

    # The fast pointer encounters a remainder of 0, so no cycle in the "list"
    if frem == 0:
        res += str((n * 10) // d)
        rem = (n * 10) % d
        while rem:
            res += str((rem * 10) // d)
            rem = (rem * 10) % d
        return res
    else:
        # Find the start point of the cycle, meanwhile, generate the non recurring part
        srem = n
        while frem != srem:
            res += str((srem * 10) // d)
            srem = (srem * 10) % d
            frem = (frem * 10) % d
        res += '('

        # Generate the recurring part
        firstTime = True
        while not (firstTime == False and srem == frem):
            firstTime = False
            res += str((srem * 10) // d)
            srem = (srem * 10) % d
        res += ')'
        return res


#def fraction_to_decimal(numerator, denominator):
#    sign = '-' if numerator * denominator < 0 else ''
#    numerator = abs(numerator)
#    denominator = abs(denominator)

#    if numerator == 0:
#        return '0'
#    elif numerator == denominator:
#        return '1'
#    elif numerator > denominator:
#        return sign + str(numerator / denominator) + fraction_to_decimal(numerator % denominator)
#    else:
#        d = 2
#        while d <= min(int(numerator ** 0.5), int(denominator ** 0.5)):
#            if numerator % d == denominator % d == 0:
#                numerator /= d
#                denominator /= d
#        if is_prime(denominator):
#            pass
#        else:
#            return str(numerator / denominator)[1:]

#def is_prime(n):
#    if n==2 or n==3: return True
#    if n%2==0 or n<2: return False
#    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
#        if n%i==0:
#            return False    

#    return True
