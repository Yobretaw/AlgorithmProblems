import sys
import math

"""
    Given a list of non negative integers, arrange them such that they form the largest number.

    For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

    Note: The result may be very large, so you need to return a string instead of an integer.
"""
def largest_number(nums):
        if not nums:
            return 0

        n = len(nums)
        nums = [str(c) for c in nums]
        nums.sort(lambda x, y: int(y + x) - int(x + y))
        return str(int(''.join(nums)))

#print largest_number([121, 12])
#print largest_number([3, 30, 34, 5, 9])
#print largest_number([1,2,4,8,16,32,64,128,256,512])
#print largest_number([128,12,320,32])
#print largest_number([0, 0])
#print largest_number([9051,5526,2264,5041,1630,5906,6787,8382,4662,4532,6804,4710,4542,2116,7219,8701,8308,957,8775,4822,396,8995,8597,2304,8902,830,8591,5828,9642,7100,3976,5565,5490,1613,5731,8052,8985,2623,6325,3723,5224,8274,4787,6310,3393,78,3288,7584,7440,5752,351,4555,7265,9959,3866,9854,2709,5817,7272,43,1014,7527,3946,4289,1272,5213,710,1603,2436,8823,5228,2581,771,3700,2109,5638,3402,3910,871,5441,6861,9556,1089,4088,2788,9632,6822,6145,5137,236,683,2869,9525,8161,8374,2439,6028,7813,6406,7519])
