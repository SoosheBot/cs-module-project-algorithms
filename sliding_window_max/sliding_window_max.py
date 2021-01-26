'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
Given an array of integers, there is a sliding window of size `k` which is moving from the left side of the array to the right, one element at a time. You can only interact with the `k` numbers in the window. Return an array consisting of the maximum value of each window of elements.

## Example
```
Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Expected Output: [3,3,5,5,6,7] 
'''

def sliding_window_max(nums, k):
    # Your code here
    #To-do--
    #Que up numbers into the k sliding window and then pop out the largest number and append it to a new array
    window = []
    arr_nums = [0] * k

    for i in range(0, len(nums) - k + 1):
        arr_nums = nums[i:i+k]
        window.append(max(arr_nums))
    
    return window
    
    
    

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
