def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    farthest = 0
    end = 0
    jumps = 0

for i in range(n - 1):
        
        farthest = max(farthest, i + arr[i])

        if i == end:
            jumps += 1    
            end = farthest  
            
          
            if end <= i:
                return -1

   
    return jumps if end >= n - 1 else -1


my_arr = [2, 3, 1, 1, 4]
result = min_jumps(my_arr)

print(f"Array: {my_arr}")
print(f"Minimum jumps needed: {result}")


# 2. Within that range, index 1 (val 3) is the best, reaching index 4.
# Total jumps: 2
