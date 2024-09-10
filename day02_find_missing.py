def find_missing_number(arr):
    '''
    Function to find the missing number in an array containing n-1 distinct integers
    within the range 1 to n.
    Uses the formula for the sum of the first n natural numbers to determine the missing number.
    '''
    
    '''
    calculates the length of the original array(n), since arr has n-1 elements
    '''
    n = len(arr) + 1
    '''
    calculates the expected sum of numbers from 1 to n using the formula n*(n+1)/2,
    also calculates actual_sum
    '''
    
    total_sum = n * (n + 1) // 2
    
    actual_sum = sum(arr)
    
    '''
    The missing number in the array is the difference between the total_sum - actual_sum
    since only one element is missing in the array.
    '''
    missing_number = total_sum - actual_sum
    
    return missing_number

def main():
    '''
    Main function to test the find_missing_number function with multiple test cases.
    Prints the result for each test case.
    '''
    
test_case1=[1,2,3,4,5,7,8,9,10]

output=find_missing_number(test_case1)

print("The missing number will be: ",output)

if __name__ == "__main__":
    main()
