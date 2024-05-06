def descend_merge_sort(nlist, start, end):
    if end - start > 1:
        mid = (start + end)//2
        descend_merge_sort(nlist, start, mid)
        descend_merge_sort(nlist, mid, end)
        merge_list(nlist, start, mid, end)
 
def merge_list(nlist, start, mid, end):
    left = nlist[start:mid]
    right = nlist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            nlist[k] = left[i]
            i = i + 1
        else:
            nlist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            nlist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            nlist[k] = right[j]
            j = j + 1
            k = k + 1

aList = [12,35,87,26,9,28,7,15]
descend_merge_sort(aList, 0, len(aList))

print(aList)

aList.reverse()
print(aList)