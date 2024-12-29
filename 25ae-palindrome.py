def isPalindrome(string):
    n = len(string)
    for i in range(0, (n // 2)):
        if string[i] != string[n - i - 1]:
            return False
    return True
