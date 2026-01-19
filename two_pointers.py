
# Palindrome
def ispalindrome(s:str)->bool:
    left,right = 0,len(s)-1
    while left < right:
        while left < right and not s[left].isalnum(): left += 1
        while left < right and not s[right].isalnum(): right -= 1
        if s[left] != s[right]:
            return False
        return True

# execution
s = "eye"
obj_pali = ispalindrome(s)
print(obj_pali)
-----------------------------------------------------------------------------------
# Reverse string

def reverse_string(s:str)->str:
    left, right = 0, len(s)-1
    s = list(s)
    while left < right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1
    return "".join(s)

# execution
m = "Balaji"
obj_rev = reverse_string(m)
print(obj_rev)
--------------------------------------------------------------------------------------
# Move Zeros to the end
def moveZeros(s):
    slow = 0
    for fast in range(len(s)):
        if s[fast] != 0:
            s[slow],s[fast] = s[fast],s[slow]
            slow += 1
    return s

# execution 
list1 = [2,0,3,0,1,7,0,0,8]
obj_move = moveZeros(list1)
print(obj_move)
------------------------------------------------------------------------------------
# two sum with sorted
def two_sum_sorted(nums:list[int],target:int)->list[int,int]:
    left, right = 0, len(nums)-1
    while left < right:
        current_sum = nums[left]+nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

# execution
list1 = list(range(10,21))
obj = two_sum_sorted(list1, 25)
print(obj)
--------------------------------------------------------------------------
# 3Sum
def three_sum(nums:list[int])->list[int,int,int]:
    res = []
    nums.sort()
    for i,j in enumerate(nums):
        if i > 0 and j == nums[i-1]:continue
        l,r = i+1, len(nums)-1
        while l<r:
            threeSum = j + nums[l]+nums[r]
            if threeSum > 0: r -= 1
            elif threeSum < 0: l += 1
            else:
                res.append([j,nums[l],nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l< r: l += 1
    return res

# execution
m = [1,0,-2,3,4,-3,-1]
obj_three = three_sum(m)
print(obj_three)
------------------------------------------------------------------------------
