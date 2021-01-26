'''
Input: a List of integers
Returns: a List of integers
Write a function that receives an array of integers and returns an array consisting of the product of all numbers in the array _except_ the number at that index. 

For example, given 
```
[1, 7, 3, 4]
```
your function should return 
```
[84, 12, 28, 21]
``` 
by calculating 
```
[7*3*4, 1*3*4, 1*7*4, 1*7*3]
'''
import math

def product_of_all_other_numbers(arr):
    # Your code here
    #To-do--
    # Loop through the array and when you land on a number ignore it and multiply the rest of the numbers in the array, return that number to a new array
    #math built-in? maybe do that head, middle, tail thing to break it up?
    #create a new array to put prods in
    new_arr = []
    for i in range(len(arr)):
        # product at the start of the list
        if i == 0:
            new_arr.append(math.prod(arr[1:]))
        # product at the end of the list
        elif i == (len(arr)-1):
            new_arr.append(math.prod(arr[:-1]))
        # product if you're in the middle of the list
        else:
            new_arr.append(math.prod(arr[:i]+arr[i+1:]))


    return new_arr

#High order components and callback functions difference -- javascript
    

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

   
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
