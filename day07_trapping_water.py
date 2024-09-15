'''
Function to trap water
'''
def trap(height):
    if len(height) < 3:
        return 0  
    
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0
    
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += max(0, right_max - height[right])
    
    return water_trapped


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])) 
print(trap([4, 2, 0, 3, 2, 5]))
print(trap([1, 1, 1])) 
print(trap([5])) 
print(trap([2, 0, 2])) 
