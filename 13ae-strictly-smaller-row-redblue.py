def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    if not len(redShirtHeights):
        return True
    isRedSmaller = True if redShirtHeights[0] < blueShirtHeights[0] else False
    for i in range(1, len(redShirtHeights)):
        if isRedSmaller:
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
        else:
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
    return True
