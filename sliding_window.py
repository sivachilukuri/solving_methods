# Maximum Sum Subarray of Size K
def MaxiSumSubarray(arr:list[int], k:int)->int:
    window_sum = sum(arr[:k])
    maxi_sum = window_sum
    for i in range(len(arr)-k):
        window_sum = window_sum - arr[i]+arr[i+k]
        maxi_sum = max(maxi_sum, window_sum)
    return maxi_sum

m = [2,1,3,8,9,7,6,5,4]
obj_maxi = MaxiSumSubarray(m,3)
print(obj_maxi)
--------------------------------------------------------------------------
# smallest_subarray
def smallest_subarray(arr, s):
    window_sum = 0
    min_len = float('inf') # Start with a huge number
    left = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]  # Add the right number
        
        # While the window sum is enough, try to shrink it from the left
        while window_sum >= s:
            # Calculate window size: (right - left + 1)
            min_len = min(min_len, right - left + 1)
            
            window_sum -= arr[left] # Remove the left number
            left += 1               # Shrink the window
            
    return min_len if min_len != float('inf') else 0