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
    #loop through array
    for x in arr:
        #in order for x to be in the non_dupe array
        if x in non_dupe:
            #we need to pop it at its index
            non_dupe.pop(non_dupe.index(x))    
        #I got this as an error so I added this to the if/else, in case there is NO repeating number, we can return whatever is in the 0th position
        # elif non_dupe is None:
        #     return None
        #if we do find this non-repeating number, append it to the non_dupe array
        else:
            non_dupe.append(x)
    
    return non_dupe
       
         


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 5, 5, 3, 3, 9, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")