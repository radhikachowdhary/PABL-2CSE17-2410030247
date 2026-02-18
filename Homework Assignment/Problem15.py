def merge_arrays(a, b):
    n = len(a)
    m = len(b)
    
  left = n - 1
    right = 0
     while left >= 0 and right < m:
        if a[left] > b[right]:
            a[left], b[right] = b[right], a[left]
            left -= 1
            right += 1
        else:
           
            break
              a.sort()
    b.sort()


arr1 = [10, 12]
arr2 = [1, 8, 9]

merge_arrays(arr1, arr2)

print(f"Modified a: {arr1}")
print(f"Modified b: {arr2}")
