def commonCharacters(strings): # O(n*m) time, O(c) space
    # n - num strings, m - length of longest string, c - number of unique characters
    # USE SET()
    cd, common, string_count = {}, [], len(strings)
    for string in strings:
        d = {}
        for c in string:
            d[c] = True
        for key in d:
            if key in cd:
                cd[key] += 1
            else:
                cd[key] = 1
    for key in cd:
        if cd[key] == string_count:
            common.append(key)
    return common
