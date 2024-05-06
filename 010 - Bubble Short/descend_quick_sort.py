def descend_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    smaller = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x < pivot]
    
    return descend_quick_sort(smaller) + equal + descend_quick_sort(larger)
