def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

    return data

def merge_sort_ascending(data):
    result = merge_sort(data)
    return result

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 19, 24, 12, 6, 129, 59, 1, 2000, 3, 56]
lst2 = [20, 21, 22, 23, 24, 25, 26, 27]
lst3 = [30, 29, 31, 33, 19, 20, 31, 21, 59]

print(merge_sort_ascending(lst1))
print(merge_sort_ascending(lst2))
print(merge_sort_ascending(lst3))
