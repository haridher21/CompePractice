def numberOfWaysToTraverseGraph(width, height): # O(min(w,h)) T O(1) S # Even better than their solution
    small = width if width <= height else height
    big = width if width > height else height
    small, big = small - 1, big - 1
    prod = 1
    for i in range(1, small + 1):
        prod *= (big + i) / (i)
    return int(prod)
