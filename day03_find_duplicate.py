def find_duplicate_number(arr):
    '''
    Function to find the duplicate number in an array containing n+1 distinct integers
    within the range 1 to n.
    Uses the formula for the sum of the first n natural numbers to determine the missing number.
    '''
    
    '''
    calculates the length of the original array(n), since arr has n+1 elements
    '''
    n = len(arr) - 1
    '''
    calculates the expected sum of numbers from 1 to n using the formula n*(n+1)/2,
    also calculates actual_sum
    '''
    
    total_sum = n * (n + 1) // 2
    
    actual_sum = sum(arr)
    
    '''
    The duplicate number in the array is the difference between the actual_sum - total_sum 
    since only one element is duplicate in the array.
    '''
    duplicate_number = actual_sum - total_sum
    return duplicate_number

def main():
    '''
    Main function to test the find_missing_number function with multiple test cases.
    Prints the result for each test case.
    '''
    
test_case1=[1, 4, 4, 2, 3]

output=find_duplicate_number(test_case1)

print("The duplicate number will be: ",output)

if __name__ == "__main__":
    main()
