def taskAssignment(k, tasks): # O(NlogN) T O(N) S
    # This is using in built way, but there's a way without it which is just as optimal, so figure that out
    sorted_with_indices = sorted(enumerate(tasks), key=lambda x: x[1])
    sorted_indices = [i for i, _ in sorted_with_indices]
    pairs = []
    for i in range(k):
        pairs.append([sorted_indices[i], sorted_indices[2 * k - i - 1]])
    return pairs
