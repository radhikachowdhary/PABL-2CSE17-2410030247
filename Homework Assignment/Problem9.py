def is_subset(a, b):
    counts = {}
    
    for num in a:
        counts[num] = counts.get(num, 0) + 1
        
    for num in b:
        if counts.get(num, 0) > 0:
            counts[num] -= 1
        else:
            return False
            
    return True


arr_a = [5, 1, 5, 8]
arr_b = [5, 5, 1]
