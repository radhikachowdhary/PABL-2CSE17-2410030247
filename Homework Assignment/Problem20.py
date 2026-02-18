def find_3_numbers_optimized(arr, target):
    n = len(arr)
    arr.sort() 
    
    
    for i in range(n - 2):
        
        
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target:
                print(f"Triplet found: {arr[i]}, {arr[left]}, {arr[right]}")
                return True
            elif current_sum < target:
                left += 1  
            else:
                right -= 1 
                
    return False
arr = [3, 1, 7, 4, 5, 9, 10]
target = 18
find_3_numbers_optimized(arr, target)
