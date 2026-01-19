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