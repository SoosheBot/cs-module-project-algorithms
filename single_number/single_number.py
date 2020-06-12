'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    #To-do
    #Figure out how to look through an array to find if there is an integer that does not show up twice -- loop?
    #If you find a single integer in the array, return that integer into a new array(?), else, continue to look through the array until you find it

    #create a new array for the not duplicate number to go in
    non_dupe = []
    #loop through array to find x
    for x in arr:
        #if x is a repeating number
        if x in non_dupe:
            #we need to pop it at its xth index so we can move on
            non_dupe.pop(non_dupe.index(x))   
        else:
            #if we do find this non-repeating number x, append it to the non_dupe array
            non_dupe.append(x)
    
    # the return is inside an array, how to convert to standalone integer? sum
    return sum(non_dupe)
       
         


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 5, 5, 3, 3, 9, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")