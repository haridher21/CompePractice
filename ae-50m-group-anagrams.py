def groupAnagrams(words):
    # Brute force, but also the only better solution
    # Can be shortened ofcourse
    d = {}
    output = []
    for i in range(len(words)):
        st = list(words[i])
        st.sort()
        st = "".join(st)
        if st in d:
            d[st].append(words[i])
        else:
            d[st] = [words[i]]
    for i in d:
        output.append(d[i])
    return output
