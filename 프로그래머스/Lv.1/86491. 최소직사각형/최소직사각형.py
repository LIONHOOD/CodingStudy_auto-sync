def solution(sizes):
    return max(sum(sizes,start=[]))*max(min(s) for s in sizes)