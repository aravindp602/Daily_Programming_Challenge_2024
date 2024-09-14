'''
The function to find the subarray whose elements sum upto zero.
the function returns the starting and ending indices of each array.
'''
def find_subarray_sumzero(arr, n):
    result = []
    prefix_sum_map = {}
    current_sum = 0
    
    prefix_sum_map[0] = [-1]
    
    for i in range(n):
        current_sum += arr[i]
        
        if current_sum in prefix_sum_map:
            for start_index in prefix_sum_map[current_sum]:
                result.append((start_index + 1, i))
        
        if current_sum in prefix_sum_map:
            prefix_sum_map[current_sum].append(i)
        else:
            prefix_sum_map[current_sum] = [i]
    
    return result

arr = [1, 2, -3, 3, -1, 2]
temp = find_subarray_sumzero(arr, len(arr))
print(temp)
