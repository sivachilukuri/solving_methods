# string compress by length
def compress(s:str)->str:
    res = []
    counter = 1
    for i in range(1,len(s)+1):
        if i < len(s) and s[i]==s[i-1]:
            counter +=1
        else:
            res.append(str(counter)+s[i-1])
            counter = 1
    return "".join(res)

# execution
obj_com = compress("aaabbccccd")
print(obj_com)

# ----------------------------------------------------------------
#Remove Adjacent Duplicates Repeatedly
# Problem
# "abbaca" → "ca"
# Pattern: Stack-based reduction
def remove_adj(s:str)->str:
    stock = []
    for ch in s:
        if stock and stock[-1]== ch:
            stock.pop()
        else:
            stock.append(ch)
    return "".join(stock)

obj_rem = remove_adj("abbach")
print(obj_rem)

#---------------------------------------------------------------
# First Non-Repeating Character
# Problem
# "swiss" → 'w'
# Pattern: Frequency + order preservation
from collections import Counter

def first_unique(s:str)->str:
    freq = Counter(s)
    for ch in freq:
        if freq[ch]==1:
            return ch
    return None

#execution
print(first_unique("swiss"))

# -----------------------------------------------------------
# Longest Substring Without Repeating Characters
# Problem
# "abcabcbb" → 3
# Pattern: Sliding window
def longest_unique(s:str)->int:
    seen = {}
    left = 0
    max_len = 0
    for right,ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch]+1
        seen[ch]= right
        max_len = max(max_len, right-left+1)
    return max_len

# unique
print(longest_unique("abcabcbb"))

# -------------------------------------------------------------------
# Decode Encoded String
# Problem
# "3[a2[c]]" → "accaccacc"
# Pattern: Stack + recursion-like behavior
def decode(s):
    stack = []
    curr = ""
    num = 0

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '[':
            stack.append((curr, num))
            curr, num = "", 0
        elif ch == ']':
            prev, n = stack.pop()
            curr = prev + curr * n
        else:
            curr += ch

    return curr

# execution
print(decode("3[a2[c]]"))
