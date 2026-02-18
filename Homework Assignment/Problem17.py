def find_common(arr1, arr2, arr3):
    n1, n2, n3 = len(arr1), len(arr2), len(arr3)
    i, j, k = 0, 0, 0
    res = []
    
    while i < n1 and j < n2 and k < n3:
        if arr1[i] == arr2[j] == arr3[k]:
            if len(res) == 0 or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
            j += 1
            k += 1
        
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
            
    return res if res else [-1]
a = [2, 2, 5, 5]
b = [2, 5, 5, 8]
c = [2, 2, 2, 5]

print(f"Common elements: {find_common(a, b, c)}")
# Output: [2, 5]
