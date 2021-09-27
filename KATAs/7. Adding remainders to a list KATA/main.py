def solve(nums, div):
    solve_list = []
    for i in nums:
        if i % div == 0:
            solve_list.append(i)
        else:
            i += (i % div)
            solve_list.append(i)
    return solve_list

