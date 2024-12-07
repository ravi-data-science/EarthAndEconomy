def max_subarray(nums):
    # Initialize both the current subarray sum and the maximum sum to the first element
    max_sum = curr_sum = nums[0]
    
    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # Update the current subarray sum: start new or continue the current subarray
        curr_sum = max(num, curr_sum + num)
        
        # Update the maximum sum if the current subarray sum is greater
        max_sum = max(max_sum, curr_sum)
    
    # Return the maximum sum found
    return max_sum

# Input array
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Output the result
print(max_subarray(nums))  # Output: 6
