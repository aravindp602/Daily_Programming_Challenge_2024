'''
Funcion to find the leader of an array where every element right to the leader should be smaller compared to it.
'''


'''
the function assumes that the each element is leader checks whether the right elements is smaller or not. if it is true it adds the leader into an array.
'''
def find_leader(arr, n):
    leader = []
    
    for i in range(n):
        is_leader = True 
        
        for j in range(i + 1, n):
            if arr[i] <= arr[j]:
                is_leader = False 
        
        if is_leader:
            leader.append(arr[i])
    
    return leader

arr =  [7, 10, 4, 10, 6, 5, 2]
ldr = find_leader(arr, len(arr))
print(ldr)
