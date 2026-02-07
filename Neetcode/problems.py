def twosum(nums,target):
    seen = {}
    for i,j in enumerate(nums):
        diff = target - j
        if diff in seen:
            return [seen[diff],i]
        seen[j] = i
    return 
m = [2,9,3,8,4,7,5,6]
print(twosum(m,12))

# leetcode - 121 : Best time to buy and sell stock
def maxProfit(prices):
    l,r = 0,1 # adjecent pointers
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r]-prices[l]
            maxP = max(maxP, profit)
        else:
            l += 1
        r += 1
    return maxP

#execution
print(maxProfit([7,1,5,4,6,3]))

#Contain Duplicate
def contain_duplicate(nums):
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

#execution
print(contain_duplicate([1,2,3,4,5,1]))

#Product of Array Exceptself - leetcode:238
def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(n-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res

#execution
print(productExceptSelf([1,2,3,4]))

# Maximum sub Array
def maxisubarray(nums):
    maxisum = nums[0]
    currsum = 0
    for i in range(len(nums)):
        if currsum < 0:
            currsum = 0
        currsum += nums[i]
        maxisum = max(maxisum, currsum)
    return maxisum

#execution
print(maxisubarray([-2,1,-3,4,-1,2,1,-5,4]))

# Maximum product subarray
def maxProduct(nums):
    res = max(nums)
    curmin,curmax = 1,1
    for n in nums:
        if n == 0:
            curmin,curmax = 1,1
        tmp = curmax * n
        curmax = max(curmax*n,curmin*n,n)
        curmin = min(tmp,curmin*n,n)
        res = max(res, curmax)
    return res

#execution
print(maxProduct([2,3,-2,4,8]))

# Find Minimum in Rotated sorted array
def findmin(nums):
    res = nums[0]
    l,r = 0,len(nums)-1
    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        m = (l + r)//2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res

#execution
print(findmin([3,4,5,1,2]))

# Search in Rotated Array - 33
def search(nums, target):
    l,r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid -1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid -1
            else:
                l = mid + 1
    return -1

# execution
print(search([3,4,5,1,2],1))

# Container with most water
def maxArea(height):
    res = 0
    l,r = 0, len(height)-1
    while l < r:
        area = (r-1)*min(height[l],height[r])
        res = max(res, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res

#execution
print(maxArea([1,8,2,3,4,5,6,8,4,6,7]))

# -----------------------------------------
