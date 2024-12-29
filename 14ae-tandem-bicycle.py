def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    if fastest:
        redShirtSpeeds.sort(reverse=fastest)
        blueShirtSpeeds.sort()
    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
    sum = 0
    for i in range(len(redShirtSpeeds)):
        sum += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return sum
