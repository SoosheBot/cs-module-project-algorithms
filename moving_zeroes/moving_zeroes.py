'''
Input: a List of integers
Returns: a List of integers
Write a function that takes an array of integers and moves each non-zero integer to the left side of the array, then returns the altered array. The order of the non-zero integers does not matter in the mutated array.
'''
def moving_zeroes(arr):
    # Your code here
    #to-do--
    #shift 0s to the left (end?) of the array then return the altered array
    #if there are no 0s, return the first element of the array
    moved = 0
    for x in range(len(arr)):
        if arr[x] != 0 and arr[moved] == 0:
            arr[x], arr[moved]= arr[moved], arr[x] 
        if arr[moved]!= 0: 
            moved+= 1
    
    
    return arr
    

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")