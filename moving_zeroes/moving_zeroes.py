'''
Input: a List of integers
Returns: a List of integers
Write a function that takes an array of integers and moves each non-zero integer to the left side of the array, then returns the altered array. The order of the non-zero integers does not matter in the mutated array.
'''
def moving_zeroes(arr):
    # Your code here
    #to-do--
    #shift 0s to the left (end?) of the array then return the altered array
    #if there are no 0s, print the array as it is
    #create a variable to house the nonzeroes

    moved = 0
    #Loop -- for x in the range of the length of array...
    for x in range(len(arr)):
        # x houses the zeroes in the equation so if x doesnt equal zero and moved DOES equal zero
        if arr[x] != 0 and arr[moved] == 0:
            #the array's order becomes the moved nonzero number to the left, and the zero to the right for the entire array
            arr[x], arr[moved] = arr[moved], arr[x] 
        if arr[moved] != 0: 
            #if moved didn't equal zero though, then jump over it to look at the next one
            moved+= 1
    
    return arr
    

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")