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

----------------------------------------------------------------------
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

----------------------------------------------------------------------
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

-----------------------------------------------------------------------------
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