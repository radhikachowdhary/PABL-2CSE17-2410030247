def max_subarray_sum(arr):

    max_so_far = arr[0]
    current_streak = 0
    
    for x in arr:
      
        current_streak += x
        
        if current_streak > max_so_far:
            max_so_far = current_streak
            
      
        if current_streak < 0:
            current_streak = 0
            
    return max_so_far


numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(numbers)) 
