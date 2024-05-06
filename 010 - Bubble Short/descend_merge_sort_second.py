def descend_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Pemisahan
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Rekursif
    left_half = descend_merge_sort(left_half)
    right_half = descend_merge_sort(right_half)
    
    # Penggabungan
    merged_arr = merge(left_half, right_half)
    
    return merged_arr

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result