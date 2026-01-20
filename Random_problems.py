# Hashset
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n-1 not in num_set:
            length = 1
            current = n
            while current+1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest

# Execution
nums = [1,3,2,5,4,102,101,103,105,106,104]
k = longest_consecutive(nums)
print(k)

# Two pointer style
def longest_consecutive1(nums):
    if not nums:
        return 0
    nums.sort()
    longest = 1 ; current = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current += 1
        elif nums[i] != nums[i-1]:
            longest = max(longest, current)
            current = 1
    return max(longest, current)

#execution
nums = [1,3,2,5,4,102,101,103,105,106,104]
k = longest_consecutive1(nums)
print(k)

# ----------------------------------------------------------------------
#Longest Substring without repeating
def longest_unique(s:str)->int:
    seen = set()
    left = best = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best

# ----------------------------------------------------------------------
# contains duplicate
def contain_duplicate(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

def contain_duplicate(nums):
    nums.sort()
    for i in range(len(nums)-2):
        if nums[i] == nums[i+1]:
            return True
    return False

# -----------------------------------------------------------------------------
# Valid Anagram
def isAnagram(s:str, t:str)->bool:
    if len(s) != len(t):
        return False
    count_s,count_t={},{}
    for i in range(len(s)):
        count_s = 1 + count_s.get(s[i],0)
        count_t = 1 + count_t.get(s[i],0)
    for c in count_s:
        if count_s[c] != count_t.get(c,0):
            return False

        
#Two Sum
def twosum(nums, target):
    h = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in h:
            return [h[diff], i ]
        h[nums[i]] = i
    return 

# Fib
def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]
print(fib(10))

def fib1(n):
    if n <= 1:
        return n
    a,b = 0,1
    for _ in range(2,n+1):
        a,b = b, a+b
    return b
print(fib1(10))

# String compression
def compress_string(s):
    if not s: return ""
    res = []
    counter = 1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            counter += 1
        else:
            res.append(str(counter)+s[i-1])
            counter = 1
    res.append(str(counter)+s[i-1])
    return "".join(res)
#execution
print(compress_string("aaabbbccddd"))

# -------------------------------------------------------
# Reverse Integer
def reverse_integer(x):
    if x < 0:
        sign = -1
        x = x * sign
    else:
        sign = 1
    res = 0
    n = x
    while n != 0:
        rem = n % 10
        res = res*10 + rem
        n = n // 10
    return res * sign

print(reverse_integer(1234))

# -----------------------------
