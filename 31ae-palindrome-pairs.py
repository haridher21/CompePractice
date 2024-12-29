# THIS SOLUTION IS NOT OPTIMAL
def semordnilap(words):
    pairs = []
    wc = len(words)
    for i in range(wc):
        ic = len(words[i])
        for j in range(i + 1, wc):
            if ic == len(words[j]):
                palin = True
                for k in range(ic):
                    if words[i][k] != words[j][ic - k - 1]:
                        palin = False
                        break
                if palin:
                    pairs.append([words[i], words[j]])
    return pairs
