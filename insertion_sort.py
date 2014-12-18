def insertionSort(ar):
    for j in range(1, len(ar)):
        key = ar[j]
        i = j - 1
        while i >= 0 and ar[i] > key:
            ar[i + 1] = ar[i]
            i -= 1
            print " ".join([str(x) for x in ar])
        ar[i + 1] = key
    print " ".join([str(x) for x in ar])
    return ar


insertionSort([2, 4, 6, 8, 3])