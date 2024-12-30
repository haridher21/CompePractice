def mergeOverlappingIntervals(intervals): # O(NlogN) T O(N) S
    if len(intervals):
        intervals.sort(key = lambda interval: interval[0])
        final = [intervals[0]]
    else:
        return []

    for i in range(1, len(intervals)):
        j = len(final) - 1
        if intervals[i][0] > final[j][1]:
            final.append(intervals[i])
            continue
        if intervals[i][1] > final[j][1]:
            final[j][1] = intervals[i][1]
    return final
