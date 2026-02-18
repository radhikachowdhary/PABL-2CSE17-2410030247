def find_kth_smallest(arr, k):
      arr.sort()
    
    return arr[k-1]


my_arr = [12, 3, 5, 7, 19, 1]
k_value = 2

result = find_kth_smallest(my_arr, k_value)

print(f"The array is: {my_arr}")
print(f"The {k_value}nd smallest
