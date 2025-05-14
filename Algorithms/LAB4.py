def selectionsort(l):
    for i in range(len(l)):
        min_idx = i
        for j in range(i + 1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
        print(l)
        l[i], l[min_idx] = l[min_idx], l[i]
    return l
arr = [64, 25, 12, 22, 11]
print(selectionsort(arr))
