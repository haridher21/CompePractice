def longestPalindromicSubstring(string):
    # O(N^2) T O(1) S
    n = len(string)
    maxPalin, maxLen = [0, 0], 0
    for i in range(n): 
        # Case 1
        left, right, length = i - 1, i, 0
        maxLen, maxPalin = checkPalin(left, right, length, string, maxLen, maxPalin)
        # Case 2
        left, right, length = i, i, -1
        maxLen, maxPalin = checkPalin(left, right, length, string, maxLen, maxPalin)
    return string[maxPalin[0]: maxPalin[1]]

"""
def longestPalindromicSubstring(string):
    # O(N^3) case
    n = len(string)
    maxPalin, maxLen = "", 0
    for i in range(n):
        st = ""
        for a in range(i, n):
            st += string[a]
            if len(st) > maxLen and palin(st):
                maxPalin, maxLen = st, len(st)
    return maxPalin
"""

def checkPalin(left, right, length, string, maxLen, maxPalin):
    n = len(string)
    while left >= 0 and right < n:
        if string[left] != string[right]:
            break
        length += 2
        if length > maxLen:
            maxLen = length
            maxPalin = [left, right + 1]
        left -= 1
        right += 1
    return maxLen, maxPalin

def palin(string): # O(N)
    n = len(string)
    if n == 1:
        return True
    for i in range(n // 2):
        if string[i] != string[n - i - 1]:
            return False
    return True
