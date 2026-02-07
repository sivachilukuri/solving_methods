# Valid Parentheses: 20
def isvalid(s):
    mapping = {")":"(","}":"{","]":"["}
    stack = []
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
#execution
print(isvalid("{]"))

# -------------------------------------------------------------
# Min Stack
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            min_val = self.min_stack[-1] 
            self.min_stack.append(min(min_val, val))
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    def top(self):
        return self.stack[-1]
    def get_min(self):
        return self.min_stack[-1]

# execution
m = MinStack()
m.push(2)
m.push(1)
print(m.get_min())
m.pop()
print(m.top())
print(m.get_min())

# Daily Temperatures (LeetCode #739)
def daily_temperatures(temp):
    n = len(temp)
    answer = [0]*n
    stack = []
    for i in range(len(temp)):
        curr_temp = temp[i]
        while stack and curr_temp > temp[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)
    return answer

# execution
p = daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
print(p)

# -------------------------------------------------------------
# Validate Stack Sequences : 946
def validatestacksequence(pushed, popped):
    stack = []
    i = 0
    for x in pushed:
        stack.append(x)
        while stack and i < len(popped) and stack[-1]==popped[i]:
            stack.pop()
            i += 1
    return len(stack) == 0
# execution
pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(validatestacksequence(pushed,popped))

# ----------------------------------------------------------------------
# Next Greater Element 1 : 496
def nextGreaterElement(nums1, nums2):
    mapping = {}
    stack = []
    for num in nums2:
        while stack and num > stack[-1]:
            smaller_num = stack.pop()
            mapping[smaller_num] = num
        stack.append(num)
    return [mapping.get(n,-1) for n in nums1]

# execution
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1,nums2))

# ---------------------------------------------
