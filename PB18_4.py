def find_sum(target: int, li: list[int]) -> tuple[int, int]:
    for i in range(len(li)):
        for j in range(len(li)):
            if li[i] + li[j] == target:
                return i, j
            
# complexity O(n^2)

def find_sum_fast(target: int, li: list[int]) -> tuple[int, int]:
    for i in li:
        wanted_value = target - i
        if wanted_value in li:
            return li.index(i), li.index(wanted_value)
        
# complexity 0(n)
