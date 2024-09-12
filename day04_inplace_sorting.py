def merge(arr1, arr2,m,n):
    '''
    Function to merge two sorted arrays arr1 and arr2 in-place without using extra space.
    
    arr1: first sorted array
    arr2: second sorted array
    '''
    '''
    function compares each element from arr1 and first element of arr2 and if arr1 element is high we swap the element and then the arr2 is sorted using insertion sort.
    '''
    for i in range(m):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            
            first = arr2[0]
            k = 1
            while k < n and arr2[k] < first:
                arr2[k - 1] = arr2[k]
                k += 1
            arr2[k - 1] = first

# Example usage:
arr1 = [1, 3, 5, 7,34]
arr2 = [2, 4, 6, 8]

merge(arr1, arr2,5,4)

print("arr1:", arr1)  
print("arr2:", arr2)  
