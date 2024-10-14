def subarray_sum(arr, target):
    sum_map = {0: 1}  # Map to store cumulative sum, starting with 0 sum
    current_sum = 0
    count = 0
    for num in arr:
        current_sum += num
        print("1:"+str(current_sum-target))
        if current_sum - target in sum_map:
            count += sum_map[current_sum - target]
        print("2:")
        print(sum_map.get(current_sum, 0) + 1)    
        sum_map[current_sum] = sum_map.get(current_sum, 0) + 1
    return count

# Example usage
arr = [1, 1, 1]
target = 2
print(subarray_sum(arr, target))  # Output: 2 (subarrays [1, 1] and [1, 1])