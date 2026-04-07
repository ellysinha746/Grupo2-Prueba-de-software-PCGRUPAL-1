def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


# Array de prueba
array = [38, 3, 1, 17, 2, 27, 9, 82, 5, 45]
print("Original:", array)
print("Ordenado:", quicksort(array))
