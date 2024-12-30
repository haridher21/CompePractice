def missingNumbers(nums): # O(N) T O(1) S
    # Had to see HINTS
    n = len(nums) + 2
    real_sum = sum(nums)
    expected_sum = (n * (n + 1)) // 2
    diff = expected_sum - real_sum
    avg = diff // 2

    smaller_half_sum = (avg * (avg + 1)) // 2
    real_smaller_half_sum = 0
    for i in nums:
        if i <= avg:
            real_smaller_half_sum += i
    missing_one = smaller_half_sum - real_smaller_half_sum
    updated_real_sum = real_sum + missing_one
    missing_two = expected_sum - updated_real_sum
    return [missing_one, missing_two]
            
    
    
    """
    # O(N^2) T O(1) S # in function search in array is hopefully logn and not N
    # Else can just do sort and see i + 1 missing for true nlogn
    n, missing = len(nums), []
    for i in range(1, n + 3):
        if i not in nums:
            missing.append(i)
    return missing
    """
