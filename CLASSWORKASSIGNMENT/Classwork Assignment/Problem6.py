def rotate_one(arr):
   n = len(arr)
    last_element = arr[n - 1]
    
for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
          arr[0] = last_element
   return arr

my_array = [10, 20, 30, 40]
print(rotate_one(my_array)) 
