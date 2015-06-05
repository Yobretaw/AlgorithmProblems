import sys
import math
import imp
from collections import defaultdict, deque

ListNode = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').Node
ll_generate_ascending_list = imp.load_source('Node', '../EPI/LinkedList/linkedlist.py').ll_generate_ascending_list

"""
    Two Sum
"""
#def twoSum(nums, target):
#        n = len(nums)
#        if n < 2:
#            return False

#        m = {}
#        for i in range(0, n):
#            val = nums[i]
#            if target - val in m:
#                return [m[target - val] + 1, i + 1]
#            m[val] = i
#        return None

    #def addTwoNumbers(l1, l2):
    #    if not l1 or not l2:
    #        return l1 if l1 else l2

    #    prev = ListNode('*')
    #    head = prev
    #    carry = 0
    #    while l1 and l2:
    #        val = l1.val + l2.val + carry
    #        carry = val / 10

    #        prev.next = ListNode(val % 10)
    #        prev = prev.next
    #        l1, l2 = l1.next, l2.next

    #    if l1 or l2:
    #        rest = l1 if l1 else l2
    #        prev.next = addTwoNumbers(ListNode(carry), rest)
    #    elif carry:
    #        prev.next = Node(1)

    #    return head.next

    #def lengthOfLongestSubstring(self, s):
    #    if not s or len(s) == 1:
    #        return 0 if not s else 1

    #    pos = {}
    #    start = -1
    #    max_len = -1
    #    for i in range(0, len(s)):
    #        char = s[i]

    #        if char in pos and pos[char] > start:
    #            start = pos[char]

    #        pos[char] = i

    #        max_len = max(max_len, i - start)
        
    #    return max_len

    #def findMedianSortedArrays(self, nums1, nums2):
    #    m, n = len(nums1), len(nums2)
        
    #    total = m + n
        
    #    if total & 1:
    #        return self.findHelp(nums1, 0, m, nums2, 0, n, total / 2 + 1)
    #    else:
    #        return ((self.findHelp(nums1, 0, m, nums2, 0, n, total / 2)) + (self.findHelp(nums1, 0, m, nums2, 0, n, total / 2 + 1))) / 2.0

    #def findHelp(self, a, i, m, b, j, n, k):
    #    if m <= 0 or n <= 0:
    #        return a[i + k - 1] if n <= 0 else b[j + k - 1]

    #    if k <= 1:
    #        return min(a[i], b[j])

    #    mid_a = a[i + m/2]
    #    mid_b = b[j + n/2]

    #    if m/2 + n/2 + 1 >= k:
    #        if mid_a > mid_b:
    #            return self.findHelp(a, i, m/2, b, j, n, k)
    #        else:
    #            return self.findHelp(a, i, m, b, j, n/2, k)
    #    else:
    #        if mid_a > mid_b:
    #            return self.findHelp(a, i, m, b, j + (n/2 + 1), n - (n/2 + 1), k - n/2 - 1)
    #        else:
    #            return self.findHelp(a, i + (m/2 + 1), m - (m/2 + 1), b, j, n, k - m/2 - 1)

    #def longestPalindrome(self, s):
    #    if not s or len(s) < 2:
    #        return s
        
    #    s1 = '#'.join(list(s))
    #    s1 = '#' + s1 + '#'

    #    n = len(s1)

    #    f = [0] * n
    #    mid = right = pos = 0
    #    l = 1
    #    for i in range(1, n):
    #        if right > i:
    #            f[i] = min(f[2 * mid - i], right - i)
    #        else:
    #            f[i] = 0

    #        while i - f[i] - 1 >= 0 and i + f[i] + 1 < n and s1[i - f[i] - 1] == s1[i + f[i] + 1]:
    #            f[i] += 1

    #        if l < f[i]:
    #            l = f[i]
    #            pos = (i - f[i]) / 2

    #        if right < i + f[i]:
    #            mid = i
    #            right = i + f[i]

    #    return s[pos:pos + l]

    #def convert(self, s, numRows):
    #    if numRows == 1:
    #        return s

    #    n = len(s)
    #    res = ''
    #    for i in range(0, numRows):
    #        j = 0
    #        idx = i
    #        while idx < n:
    #            idx += s[idx]

    #            if i != 0 and i != numRows - 1 and idx + (numRows - i - 1) * 2 < n:
    #                res += s[idx + (numRows - i - 1) * 2]

    #            j += 1
    #            idx = (2 * numRows- 2) * j + i

    #    return res

    #def reverse(self, x):
    #    if x == 0:
    #        return x

    #    sign = -1 if x < 0 else 1
    #    x = max(x, -x)

    #    res = 0
    #    while x:
    #        if (INT_MAX - x % 10) < res:
    #            return INT_MAX

    #        res = 10 * res + x % 10
    #        x /= 10

    #    return res * sign

    #def myAtoi(self, s):
    #    if not s:
    #        return 0

    #    res = 0
    #    s = s.strip()
    #    i = 0
    #    sign = 1

    #    if s[0] == '+' or s[0] == '-':
    #        sign = 1 if s[0] == '+' else -1
    #        i += 1

    #    while i < len(s):
    #        if s[i].isdigit():
    #            val = ord(s[i]) - ord('0')
    #            if sign > 0 and (INT_MAX - val) / 10 < res:
    #                return INT_MAX
    #            elif sign < 0 and (INT_MAX + 1 - val) / 10 < res:
    #                return INT_MIN
    #            else:
    #                res = 10 * res + val
    #            i += 1
    #        else:
    #            return sign * res
    #    return sign * res

    #def isPalindrome(self, x):
    #    if x < 0:
    #        return False

    #    d = 1
    #    while 10 * d <= x:
    #        d *= 10

    #    while x > 0:
    #        if x / d != x % 10:
    #            return False
            
    #        x %= d
    #        x /= 10
    #        d /= 100
        
    #    return True
                
    #def __init__(self):
    #    self.m = {}
    #    pass

    #def isMatch(self, s, p):
    #    m = self.m

    #    if (s, p) in m:
    #        return m[(s, p)]

    #    if p == "":
    #        return s == ""

    #    if len(p) == 1 or p[1] != '*':
    #        if not s:
    #            return False
    #        res = self.isMatch(s[1:], p[1:]) if p[0] == '.' or p[0] == s[0] else False
    #        m[(s, p)] = res
    #        return res
        
    #    if self.isMatch(s, p[2:]):
    #        m[(s, p)] = True
    #        return True

    #    i = 0
    #    while i < len(s) and (p[0] == '.' or p[0] == s[i]):
    #        if self.isMatch(s[i + 1:], p[2:]):
    #            m[(s, p)] = True
    #            return True
    #        i += 1
        
    #    m[(s, p)] = False
    #    return False

    #def maxArea(self, height):
    #    if not height or len(height) < 2:
    #        return 0

    #    start = 0
    #    end = len(height) - 1
    #    max_area = 0
    #    while start < end:
    #        max_area = max((end - start) * min(height[start], height[end]), max_area)

    #        if height[start] < height[end]:
    #            start += 1
    #        else:
    #            end -= 1

    #    return max_area

    #def intToRoman(self, num):
    #    m = {
    #        1: 'I',
    #        4: 'IV',
    #        5: 'V',
    #        9: 'IX',
    #        10: 'X',
    #        40: 'XL',
    #        50: 'L',
    #        90: 'XC',
    #        100: 'C',
    #        400: 'CD',
    #        500: 'D',
    #        900: 'CM',
    #        1000: 'M'
    #    }

    #    d = 1
    #    while 10 * d <= num:
    #        d *= 10

    #    res = ''
    #    while num > 0:
    #        val = num / d
    #        if val * d in m:
    #            res += m[val * d]
    #        else:
    #            if val < 4:
    #                res += m[d] * val
    #            else:
    #                res += m[val - 5] + (5 - d) * m[d]
    #        num %= d
    #        d /= 10
    #    return res

    #def romanToInt(self, s):
    #    if not s:
    #        return 0

    #    m = {
    #        'I': 1,
    #        'V': 5,
    #        'X': 10,
    #        'L': 50,
    #        'C': 100,
    #        'D': 500,
    #        'M': 1000
    #    }

    #    res = 0
    #    for i in range(0, len(s)):
    #        if i > 0 and m[s[i]] > m[s[i - 1]]:
    #            res += (m[s[i]] - 2 * m[s[i - 1]])
    #        else:
    #            res += m[s[i]]
    #    return res

    #def longestCommonPrefix(self, strs):
    #    n = len(strs)
    #    if n < 2:
    #        return '' if not n else strs[0]

    #    l = len(strs[0]) - 1
    #    for i in range(1, len(strs)):
    #        s = strs[i]
    #        l = min(l, len(strs[i]) - 1)

    #        if l < 0:
    #            return ''

    #        j = 0
    #        while j <= l and s[j] == strs[0][j]:
    #            j += 1
    #        l = j - 1

    #    return strs[0][:l + 1]

    #def threeSum(self, nums):
    #    n = len(nums)
    #    if n < 3:
    #        return []

    #    nums.sort()
    #    res = []
    #    start = 0
    #    while start < n - 2:
    #        mid = start + 1
    #        end = n - 1

    #        while mid < end:
    #            print nums[start], nums[end], nums[mid]
    #            total = nums[start] + nums[end] + nums[mid]
    #            if total == 0:
    #                res.append([nums[start], nums[mid], nums[end]])
    #                mid += 1
    #                end -= 1
    #                while mid < end and nums[mid] == nums[mid - 1]:
    #                    mid += 1
    #                while mid < end and nums[end] == nums[end + 1]:
    #                    end -= 1
    #            elif total > 0:
    #                end -= 1
    #            else:
    #                mid += 1


    #        while start < n - 2 and nums[start] == nums[start + 1]:
    #            start += 1
    #        start += 1
    #    return res

    #def threeSumClosest(self, nums, target):
    #    n = len(nums)
    #    if n < 3:
    #        return 0

    #    nums.sort()
    #    res = 0
    #    start = 0
    #    min_distance = sys.maxint
    #    while start < n - 2:
    #        mid = start + 1
    #        end = n - 1

    #        while mid < end:
    #            total = nums[start] + nums[mid] + nums[end]
    #            diff = total - target
    #            if abs(diff) <= min_distance:
    #                res = total
    #                min_distance = abs(diff)
                    
    #            if diff > 0:
    #                end -= 1
    #                while mid < end and nums[end] == nums[end + 1]:
    #                    end -= 1
    #            else:
    #                mid += 1
    #                while mid < end and nums[mid] == nums[mid - 1]:
    #                    mid += 1


    #        while start < n - 2 and nums[start] == nums[start + 1]:
    #            start += 1
    #        start += 1
    #    return res

    #def letterCombinations(self, digits):
    #    if not digits:
    #        return []

    #    m = {
    #        1: [],
    #        2: ['a', 'b', 'c'],
    #        3: ['d', 'e', 'f'],
    #        4: ['g', 'h', 'i'],
    #        5: ['j', 'k', 'l'],
    #        6: ['m', 'n', 'o'],
    #        7: ['p', 'q', 'r', 's'],
    #        8: ['t', 'u', 'v'],
    #        9: ['w', 'x', 'y', 'z']
    #    }

    #    res = []
    #    n = len(digits)

    #    res = list(m[int(digits[0])])

    #    for i in range(1, n):
    #        arr = m[int(digits[i])]
    #        tmp = []
    #        for s in res:
    #            for c in arr:
    #                tmp.append(s + c)
    #        res = tmp

    #    return res

    #def fourSum(self, nums, target):
    #    n = len(nums)
    #    if n < 4:
    #        return []

        
    #    nums.sort()
    #    start = 0
    #    res = []
    #    while start < n - 3:
    #        tmp = self.threeSumTarget(nums[start + 1:], target - nums[start])
    #        for t in tmp:
    #            res.append([nums[start]] + t)

    #        while start < n - 3 and nums[start] == nums[start + 1]:
    #            start += 1
    #        start += 1

    #    return res

    #def threeSumTarget(self, nums, target):
    #    n = len(nums)
    #    if n < 3:
    #        return []

    #    nums.sort()
    #    res = []
    #    start = 0
    #    while start < n - 2:
    #        mid = start + 1
    #        end = n - 1

    #        while mid < end:
    #            diff = nums[start] + nums[end] + nums[mid] - target
    #            if diff == 0:
    #                res.append([nums[start], nums[mid], nums[end]])
    #                mid += 1
    #                end -= 1
    #                while mid < end and nums[mid] == nums[mid - 1]:
    #                    mid += 1
    #                while mid < end and nums[end] == nums[end + 1]:
    #                    end -= 1
    #            elif diff > 0:
    #                end -= 1
    #            else:
    #                mid += 1


    #        while start < n - 2 and nums[start] == nums[start + 1]:
    #            start += 1
    #        start += 1
    #    return res

    #def removeNthFromEnd(self, head, n):
    #    if not head:
    #        return None

    #    slow = fast = head
    #    while n >= 0 and fast:
    #        fast = fast.next
    #        n -= 1

    #    if not n and not fast:
    #        return head.next

    #    while fast:
    #        slow, fast = slow.next, fast.next

    #    slow.next = slow.next.next

    #    return head

    #def isValid(self, s):
    #    if not s:
    #        return True

    #    if len(s) & 1:
    #        return False

    #    n = len(s)
    #    st = []
    #    for c in s:
    #        if c == '(' or c == '[' or c == '{':
    #            st.append(c)
    #        elif not st:
    #            return False
    #        else:
    #            if st[-1] == '(' and c == ')' or\
    #                    st[-1] == '[' and c == ']' or\
    #                    st[-1] == '{' and c == '}':
    #                        st.pop()
    #            else:
    #                return False
    #    return len(st) == 0

    #def mergeTwoLists(self, l1, l2):
    #    if not l1 or not l2:
    #        return l1 if l1 else l2
        
    #    dummy = ListNode('*')
    #    prev = dummy
    #    while l1 and l2:
    #        if l1.val < l2.val:
    #            prev.next = l1
    #            l1 = l1.next
    #        else:
    #            prev.next = l2
    #            l2 = l2.next
    #        prev = prev.next
        
    #    if l1 or l2:
    #        prev.next = l1 if l1 else l2

    #    return dummy.next
        
    #def generateParenthesis(self, n):
    #    if not n:
    #        return []

    #    res = []
    #    self.generateParenthesisHelp(n, 0, '', res)
    #    return res

    #def generateParenthesisHelp(self, n, open_count, curr, res):
    #    if open_count == n and len(curr) == 2 * n:
    #        res.append(curr)
    #        return
        
    #    if open_count < n:
    #        self.generateParenthesisHelp(n, open_count + 1, curr + '(', res)
    #    if open_count > len(curr) - open_count:
    #        self.generateParenthesisHelp(n, open_count, curr + ')', res)

    #def mergeKLists(self, lists):
    #    if not lists:
    #        return None
    #    if len(lists) <= 2:
    #        return lists[0] if len(lists) == 1 else self.mergeTwoLists(lists[0], lists[1])

    #    n = len(lists)
    #    res = []
    #    i = 0
    #    while i < n:
    #        if i + 1 < n:
    #            res.append(self.mergeKLists([lists[i], lists[i + 1]]))
    #        else:
    #            res.append(lists[i])
    #        i += 2
    #    return self.mergeKLists(res)

    #def mergeTwoLists(self, l1, l2):
    #    if not l1 or not l2:
    #        return l1 if l1 else l2
        
    #    dummy = ListNode('*')
    #    prev = dummy
    #    while l1 and l2:
    #        if l1.val < l2.val:
    #            prev.next = l1
    #            l1 = l1.next
    #        else:
    #            prev.next = l2
    #            l2 = l2.next
    #        prev = prev.next
        
    #    if l1 or l2:
    #        prev.next = l1 if l1 else l2

    #    return dummy.next

    #def swapPairs(self, head):
    #    if not head or not head.next:
    #        return head

    #    #new_head = head.next
    #    #tmp = new_head.next
    #    #new_head.next = head
    #    #head.next = self.swapPairs(tmp)
    #    #return new_head

    #    new_head = head.next
    #    rest = head.next.next
    #    new_head.next = head

    #    curr = rest
    #    prev = head

    #    while curr and curr.next:
    #        prev.next = curr.next
    #        tmp = curr.next.next
    #        curr.next.next = curr

    #        prev = prev.next.next
    #        curr = tmp

    #    prev.next = curr
    #    return new_head

    #def findSubstring(self, s, words):
    #    from collections import defaultdict
    #    if not s or not words:
    #        return []

    #    l = len(words[0])
    #    n = len(words)

    #    m = defaultdict(int)
    #    for word in words:
    #        m[word] += 1

    #    res = []
    #    for i in range(0, len(s) - n*l + 1):
    #        j = i
    #        total_count = 0
    #        seen = {}
    #        for j in range(i, i + n * l, l):
    #            w = s[j:j + l]
    #            if not w in m or m[w] == 0:
    #                break
    #            else:
    #                if not w in seen:
    #                    seen[w] = m[w]
    #                m[w] -= 1
    #                total_count += 1
    #        if total_count == n:
    #            res.append(i)
    #        for key in seen:
    #            m[key] = seen[key]
    #    return res

    #def nextPermutation(self, nums):
    #    if not nums or len(nums) < 2:
    #        return

    #    n = len(nums)

    #    i = n - 1
    #    while i > 0 and nums[i] <= nums[i - 1]:
    #        i -= 1

    #    i -= 1
    #    if i < 0:
    #        i, j = 0, n - 1
    #        while i < j:
    #            nums[i], nums[j] = nums[j], nums[i]
    #            i += 1
    #            j -= 1
    #        return

    #    j = i + 1
    #    while j < n and nums[j] > nums[i]:
    #        j += 1

    #    j -= 1
    #    nums[i], nums[j] = nums[j], nums[i]

    #    i += 1
    #    j = n - 1
    #    while i < j:
    #        nums[i], nums[j] = nums[j], nums[i]
    #        i += 1
    #        j -= 1

    #def longestValidParentheses(self, s):
    #    if not s or len(s) < 2:
    #        return 0

    #    n = len(s)
    #    max_len = 0
    #    start = count = 0
    #    for i in range(0, n):
    #        if s[i] == '(':
    #            count += 1
    #        else:
    #            count -= 1
    #            if count == 0:
    #                max_len = max(max_len, i - start + 1)
    #            elif count < 0:
    #                start = i + 1
    #                count = 0

    #    end = n - 1
    #    count = 0
    #    for i in reversed(range(0, n)):
    #        if s[i] == ')':
    #            count += 1
    #        else:
    #            count -= 1
    #            if count == 0:
    #                max_len = max(max_len, end - i + 1)
    #            elif count < 0:
    #                end = i - 1
    #                count = 0
    #    return max_len

    #def search(self, nums, target):
    #    if not nums or len(nums) < 2:
    #        return -1 if not nums or nums[0] != target else 0

    #    start = 0
    #    end = len(nums) - 1
    #    while start <= end:
    #        mid = (start + end) / 2
    #        if nums[mid] == target:
    #            return mid
    #        elif nums[mid] > nums[end]:
    #            if nums[start] <= target < nums[mid]:
    #                end = mid - 1
    #            else:
    #                start = mid + 1
    #        else:
    #            if nums[mid] < target <= nums[end]:
    #                start = mid + 1
    #            else:
    #                end = mid - 1
    #    return -1

    #def searchRange(self, nums, target):
    #    if not nums:
    #        return [-1, -1]

    #    return [self.searchLowerBound(nums, target), self.searchUpperBound(nums, target)]

    #def searchLowerBound(self, a, target):
    #    if not a or len(a) < 2:
    #        return -1 if not a or a[0] != target else 0

    #    n = len(a)
    #    start, end = 0, len(a) - 1
    #    while start <= end:
    #        mid = (start + end) / 2
            
    #        if a[mid] == target:
    #            if mid > 0 and a[mid - 1] == target:
    #                end = mid - 1
    #            else:
    #                return mid
    #        elif a[mid] > target:
    #            end = mid - 1
    #        else:
    #            start = mid + 1
    #    return -1

    #def searchUpperBound(self, a, target):
    #    if not a or len(a) < 2:
    #        return -1 if not a or a[0] != target else 0

    #    n = len(a)
    #    start, end = 0, len(a) - 1
    #    while start <= end:
    #        mid = (start + end) / 2
            
    #        if a[mid] == target:
    #            if mid < n - 1 and a[mid + 1] == target:
    #                start = mid + 1
    #            else:
    #                return mid
    #        elif a[mid] > target:
    #            end = mid - 1
    #        else:
    #            start = mid + 1
    #    return -1

    #def searchInsert(self, nums, target):
    #    if not nums:
    #        return 0
        
    #    n = len(nums)
    #    start, end = 0, n - 1
    #    while start <= end:
    #        mid = (start + end) / 2
    #        if nums[mid] == target:
    #            return mid
    #        elif nums[mid] > target and (mid == 0 or nums[mid - 1] < target):
    #            return mid
    #        elif nums[mid] < target and (mid == n - 1 or nums[mid + 1] > target):
    #            return mid + 1
    #        elif nums[mid] > target:
    #            end = mid - 1
    #        else:
    #            start = mid + 1
    #    return 0

    #def isValidSudoku(self, board):
    #    if not board or not board[0]:
    #        return True

    #    # 1 - 9 -> 2 -> 23
    #    PRIMES = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]

    #    rows = [1] * len(board)
    #    cols = [1] * len(board[0])
    #    square = [1] * 9

    #    for i in range(0, len(board)):
    #        for j in range(0, len(board[0])):
    #            if board[i][j] == '.':
    #                continue

    #            d = PRIMES[int(board[i][j])]
    #            if rows[i] % d == 0 or cols[j] % d == 0 or square[i - i % 3 + j / 3] % d == 0:
    #                return False
                
    #            rows[i] *= d
    #            cols[j] *= d
    #            square[i - i % 3 + j / 3] *= d

    #    return True

#class Solution:
#    def __init__(self):
#        self.rows = [1] * 9
#        self.cols = [1] * 9
#        self.square = [1] * 9
#    # @param {character[][]} board
#    # @return {void} Do not return anything, modify board in-place instead.
#    def solveSudoku(self, board):
#        availables = []
#        PRIMES = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
#        for i in range(0, 9):
#            board[i] = list(board[i])

#        for i in range(0, 9):
#            for j in range(0, 9):
#                if board[i][j] == '.':
#                    availables.append((i, j))
#                else:
#                    val = PRIMES[int(board[i][j])]
#                    self.rows[i] *= val
#                    self.cols[j] *= val
#                    self.square[i-i%3+j/3] *= val
        
#        self.solver(board, availables)

#        for i in range(0, 9):
#            board[i] = ''.join(board[i])

#    def solver(self, board, availables):
#        if not availables:
#            return True

#        i, j = availables[-1]
#        availables.pop()
#        PRIMES = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
#        for x in range(1, 10):
#            val = PRIMES[x]
#            if self.rows[i] % val != 0 and self.cols[j] % val != 0 and self.square[i-i%3+j/3] % val != 0:
#                board[i][j] = str(x)

#                self.rows[i] *= val
#                self.cols[j] *= val
#                self.square[i-i%3+j/3] *= val

#                if self.solver(board, availables):
#                    return True

#                self.rows[i] /= val
#                self.cols[j] /= val
#                self.square[i-i%3+j/3] /= val

#                board[i][j] = '.'
#        availables.append((i, j))
#        return False

    #def countAndSay(self, n):
    #    if n == 1:
    #        return '1'

    #    res = '1'
    #    for i in range(1, n):
    #        res += '_'
    #        tmp = []

    #        j = 0
    #        count = 1
    #        for j in range(1, len(res)):
    #            if res[j] != res[j - 1]:
    #                tmp.extend([count, res[j - 1]])
    #                count = 1
    #            else:
    #                count += 1
    #        res = ''.join(map(str, tmp))
    #    return res

    #def combinationSum(self, candidates, target):
    #    if not candidates:
    #        return []

    #    candidates.sort()
    #    res = []
    #    self.help(candidates, target, 0, [], res)
    #    return res

    #def help(self, arr, target, idx, path, res):
    #    if idx == len(arr) or sum(path) >= target:
    #        if sum(path) == target:
    #            res.append(list(path))
    #        return

    #    if arr[idx] > target:
    #        return

    #    self.help(arr, target, idx + 1, path, res)

    #    if sum(path) >= target:
    #        return

    #    path.append(arr[idx])
    #    self.help(arr, target, idx, path, res)
    #    path.pop()

    #def combinationSum2(self, candidates, target):
    #    if not candidates:
    #        return []

    #    candidates.sort()
    #    res = []
    #    self.help(candidates, target, 0, [], res, 0)
    #    return res

    #def help(self, arr, target, idx, path, res, total):
    #    if idx == len(arr) or total >= target:
    #        if total == target:
    #            res.append(list(path))
    #        return

    #    i = idx
    #    while i < len(arr) - 1 and arr[i] == arr[i + 1]:
    #        i += 1
    #    self.help(arr, target, i + 1, path, res, total)

    #    path.append(arr[idx])
    #    self.help(arr, target, idx + 1, path, res, total + arr[idx])
    #    path.pop()

    #def firstMissingPositive(self, nums):
    #    if not nums:
    #        return 1

    #    for i in range(0, len(nums)):
    #        j = i
    #        while nums[j] > 0 and nums[j] <= len(nums) and nums[j] != j + 1 and nums[j] != nums[nums[j] - 1]:
    #            t = nums[j] - 1
    #            nums[j], nums[t] = nums[t], nums[j]

    #    for i in range(0, len(nums)):
    #        if nums[i] != i + 1:
    #            return i + 1

    #    return len(nums) + 1

    #def quicksort(self, arr):
    #    self.quicksortHelp(arr, 0, len(arr) - 1)

    #def quicksortHelp(self, arr, start, end):
    #    if start < end:
    #        mid = self.partition(arr, start, end)

    #        self.quicksortHelp(arr, start, mid - 1)
    #        self.quicksortHelp(arr, mid + 1, end)

    #def partition(self, arr, start, end):
    #    pivotal = arr[start]

    #    left = start + 1
    #    right = end
    #    done = False

    #    while not done:
    #        while left <= right and arr[left] <= pivotal:
    #            left += 1

    #        while left <= right and arr[right] >= pivotal:
    #            right -= 1

    #        if right < left:
    #            done = True
    #        else:
    #            arr[left], arr[right] = arr[right], arr[left]

    #    arr[start], arr[right] = arr[right], arr[start]
    #    return right

    #def trap(self, height):
    #    n = len(height)       

    #    if n <= 2:
    #        return 0

    #    left, right = 0, n - 1
    #    left_max, right_max = height[left], height[right]
        
    #    left += 1
    #    right -= 1
    #    res = 0
    #    while left <= right:
    #        left_max = max(left_max, height[left])
    #        right_max = max(right_max, height[right])

    #        if left_max > right_max:
    #            res += right_max - height[right]
    #            right -= 1
    #        else:
    #            res += left_max - height[left]
    #            left += 1
        
    #    return res

    #def multiply(self, num1, num2):
    #    if not num1 or not num2:
    #        return num1 if num1 else num2
        
    #    num1 = num1[::-1]
    #    num2 = num2[::-1]
    #    m, n = len(num1), len(num2)
    #    res = [0] * (m + n + 1)
    #    for i in range(0, m):
    #        for j in range(0, n):
    #             res[i + j] += int(num1[i]) * int(num2[j])
    #             res[i + j + 1] += res[i + j] / 10
    #             res[i + j] %= 10

    #    print res       
    #    res[m + n]  = res[m + n - 1] / 10
    #    res[m + n - 1] %= 10
    #    while res and res[-1] == 0:
    #        res.pop()
    #    return ''.join(map(str, res[::-1])) if res else '0'

#class Solution:
#    def __init__(self):
#        self.m = {}

#    # @param {string} s
#    # @param {string} p
#    # @return {boolean}
#    def isMatch(self, s, p):
#        if not p:
#            return not s

#        m = self.m
#        key = (s, p)

#        if key in m:
#            return m[key]

#        if p[0] != '*':
#            m[key] = s and (s[0] == p[0] or p[0] == '?') and self.isMatch(s[1:], p[1:])
#            return m[key]
        
#        if self.isMatch(s, p[1:]):
#            m[key] = True
#            return m[key]
        
#        j = 0
#        while j < len(p) and p[j] == '*':
#            j += 1

#        for i in range(0, len(s)):
#            if self.isMatch(s[i + 1:], p[j:]):
#                m[key] = True
#                return m[key]
        
#        m[key] = False
#        return False

#    def isMatch2(self, s, p):
#        if not p:
#            return not s

#        m, n = len(s), len(p)
#        i = j = 0
#        last_x = 0
#        last_y = -1
#        while i < m:
#            if j < n and (p[j] == '?' or p[j] == s[i]):
#                i += 1
#                j += 1
#            elif j < n and p[j] == '*':
#                last_x = i
#                last_y = j
#                j += 1
#            elif last_y >= 0:
#                i = last_x + 1
#                last_x += 1
#                j = last_y + 1
#            else:
#                return False
        
#        if i < m:
#            return False

#        while j < n and p[j] == '*':
#            j += 1

#        return j == n

    #def jump(self, nums):
    #    if not nums or len(nums) == 1:
    #        return 0

    #    step = 0
    #    curr_pos = right_most = 0
    #    for i in range(0, len(nums)):
    #        if curr_pos >= len(nums):
    #            return step
    #        if curr_pos < i:
    #            if right_most < i:
    #                return -1
    #            curr_pos = right_most
    #            step += 1
    #        right_most = max(right_most, i + nums[i])
    #    return step

    #def permute(self, nums):
    #    if len(nums) < 2:
    #        return [] if not nums else [nums]

    #    res = []
    #    self.permute_help(nums, 0, res)
    #    return res

    #def permute_help(self, nums, idx, res):
    #    if idx == len(nums):
    #        res.append(list(nums))
    #        return

    #    seen = set()
    #    for i in range(idx, len(nums)):
    #        if nums[i] in seen:
    #            continue
    #        seen.add(nums[i])

    #        nums[idx], nums[i] = nums[i], nums[idx]
    #        self.permute_help(nums, idx + 1, res)
    #        nums[idx], nums[i] = nums[i], nums[idx]

    #def rotate(self, matrix):
    #    if not matrix or not matrix[0]:
    #        return

    #    m, n = len(matrix), len(matrix[0])
    #    for i in range(0, m/2):
    #        for j in range(0, n):
    #            matrix[i][j], matrix[m - 1 - i][j] = matrix[m - 1 - i][j], matrix[i][j]

    #    for i in range(1, m):
    #        for j in range(0, i):
    #            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    #def anagrams(self, arr):
    #    if len(arr) < 2:
    #        return []
        
    #    from collections import defaultdict
    #    m = defaultdict(list)
    #    for s in arr:
    #        ss = ''.join(sorted(s))
    #        if ss in m:
    #            m[ss].append(s)
    #        else:
    #            m[ss] = [s]

    #    res = []
    #    for key in m:
    #        if len(m[key]) > 1:
    #            res.extend(m[key])
    #    return res

    #def myPow(self, x, n):
    #    if 0 <= n <= 1:
    #        return x if n else 1

    #    sign = 1 if n > 0 else -1
    #    n = max(n, -n)
    #    res = 1
    #    while n > 0:
    #        if n & 1:
    #            res *= x

    #        x *= x
    #        n >>= 1

    #    return res if sign > 0 else 1.0 / res

INT_MAX = 2 ** 31 - 1
INT_MIN = -INT_MAX - 1

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        res = []
        path = [-1] * n
        self.solveNQueensHelp(n, 0, path, res)
        return res
    
    def solveNQueensHelp(self, n, row, path, res):
        if row == n:
            res.append(self.generateGrid(path))
            return

        for col in range(0, n):
            if self.isValidPut(path, row, col):
                path[row] = col
                self.solveNQueensHelp(n, row + 1, path, res)
                path[row] = -1
        return
    
    def isValidPut(self, path, row, col):
        for v in path:
            if v == col:
                return False

        i = 1
        while row - i >= 0:
            if path[row - i] == col - i or path[row - i] == col + i:
                return False
            i += 1

        return True


    def generateGrid(self, path):
        n = len(path)
        grid = [None] * n
        for i in range(0, n):
            grid[i] = ['.'] * n
        
        print path
        for i in range(0, n):
            for j in range(0, n):
                if path[i] == j:
                    grid[i][j] == 'Q'
        return grid

    def printGrid(self, grid):
        for line in grid:
            print ''.join(line)


for g in Solution().solveNQueens(4):
    Solution().printGrid(g)
    print '-'*10
