def zeroSumSubarray(nums): # O(N) T S
    running_sum, d = 0, {}
    for i in nums:
        running_sum += i
        if running_sum in d:
            return True
        d[running_sum] = True
    return False if running_sum  or (not nums) else True



    """
    #O(N^2) T O(N) S
    n = len(nums)
    if n == 0:
        return False
    for sub_array_size in range(1, n + 1):
        sub_array_sum = 0
        for j in range(sub_array_size):
            sub_array_sum += nums[j]
        if sub_array_sum == 0:
            return True

        for j in range(sub_array_size, n):
            sub_array_sum += nums[j] - nums[j - sub_array_size]
            if sub_array_sum == 0:
                return True
    return False
    """
