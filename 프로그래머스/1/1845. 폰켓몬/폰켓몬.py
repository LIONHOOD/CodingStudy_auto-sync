def solution(nums):
    N = len(nums)
    n = N//2
    if n<=len(set(nums)):
        return n
    else:
        return len(set(nums))