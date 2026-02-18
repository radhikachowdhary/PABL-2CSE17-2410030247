def search_insert(nums, target):
       low = 0
    high = len(nums) - 1
    
    while low <= high:
        
        mid = (low + high) // 2
        
       
        if nums[mid] == target:
            return mid
        
        
        elif nums[mid] < target:
            low = mid + 1
            
       
        else:
            high = mid - 1
            

    return low


nums = [10, 20, 30, 40, 50]
target = 25
print(search_insert(nums, target)) 
