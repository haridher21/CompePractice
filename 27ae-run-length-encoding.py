def runLengthEncoding(string):
    i, n, new_string = 0, len(string), ""
    while i < n:
        c, count = string[i], 1
        while i < (n - 1) and string[i + 1] == c:
            i += 1
            count += 1
            if count == 10:
                new_string += "9" + c
                count = 1
        new_string += str(count) + c
        i += 1
    return new_string
