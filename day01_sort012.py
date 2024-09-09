'''
The function is sort the array which contains only 0 1 2 as the elements in the ascending order without using any extra space and should be linear in time. ie O(n).
Here we use Dutch National Flag Algorithm for the implementation.
'''

def sort012(arr):
    '''
    Pointers are intialized as low ,mid and high.
    '''
    low, mid, high = 0, 0, len(arr) - 1
    
    '''
    loop to traverse through the array.
    In this loop we will check whether the mid element is 0. if yes the mid element will be swapped with low and low ,mid pointers are incremented. if not 0 check whether
    it is 1 or not. if it is one keep as it is and updated the mid value by 1. else it will 2 and will swap mid and high. then increments mid and high pointers.
    '''
    while mid <= high:
        if arr[mid] == 0: 
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1: 
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr

def main():
    
    arr = [0, 1, 2, 1, 0, 2, 1, 0]
    print("array before sorting :", arr)
    print(" ")
    sorted_arr = sort012(arr)
    print("array after sorting :  ", sorted_arr)

if __name__ == "__main__":
    main()
