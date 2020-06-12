'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cookie_tin=None):

    if cookie_tin == None:
        cookie_tin = [0] * (n + 1)
    if n <= 1:
        cookie_tin[n] = 1
    elif n == 2:
        cookie_tin[n] = 2
    elif cookie_tin[n] == 0:
        cookie_tin[n] = eating_cookies(n - 1, cookie_tin) + eating_cookies(n - 2, cookie_tin) + eating_cookies(n - 3, cookie_tin)

    return cookie_tin[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
