def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


# Array de prueba
array = [3,1,5,3,10,13,9,11,1,21,4]
print("Original:", array)
print("Ordenado:", quicksort(array))
