'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    #To-do
    #Figure out how to look through an array to find if there is an integer that does not show up twice -- loop?
    #If you find a single integer in the array, return that integer, else, continue to look through the array

    single_int = set(arr)
    return single_int


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")