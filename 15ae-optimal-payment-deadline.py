def optimalFreelancing(jobs):
    joblist = [None for _ in range(7)]
    jobs = sorted(jobs, key=lambda x: -x["payment"])
    profit, i, n = 0, 0 , len(jobs)
    while i < n:
        day, pay = jobs[i]["deadline"], jobs[i]["payment"]
        cur_idx = day - 1 if day <= 7 else 6
        while cur_idx >= 0 and joblist[cur_idx]:
            cur_idx -= 1
        if cur_idx >= 0:
            joblist[cur_idx] = jobs[i]
            profit += pay
        i += 1
    return profit
