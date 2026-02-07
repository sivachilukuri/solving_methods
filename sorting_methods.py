# Bubble sort
def bubble_sort(nums):
    """we are compare adjcent elements and setup large element at the end of list
    Time Complexity: O(n^2) because of the nested loops.
    Space Complexity: O(1) because you are sorting "in-place" without extra memory."""
    n = len(nums)
    for i in range(n):
        # here we are reducing lenth of list beacuse every iteration setup fix last element
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums
l = [9,1,8,2,7,3,6,4,5]
obj = bubble_sort(l)
print(obj)

# Bubble sort optimazation
def bubble_sort_opt(nums):
    n = len(nums)
    counter = 0
    for i in range(n):
        swap = False
        counter += 1
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                swap = True
        if not swap:
            break
    print(counter)
    return nums
k = [9,1,8,2,7,3,6,4,5]
obj1 = bubble_sort_opt(k)
print(obj1)

# Selection Sort
def selection_sort(nums):
    """
    selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums
f = [2,8,9,3,1,7,4,6,5]
obj2 = selection_sort(f)
print(obj2)

# Insertion_sort
def insertion_sort(nums):
    """
    We assume that the first card is already sorted then, we select an unsorted card. 
    If the unsorted card is greater than the card in hand, it is placed on the right otherwise, to the left. 
    In the same way, other unsorted cards are taken and put in their right place.
    """
    for i in range(1,len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

f = [2,8,9,3,1,7,4,6,5]
obj3 = insertion_sort(f)
print(obj3)

