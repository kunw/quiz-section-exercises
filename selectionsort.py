def selectionsort(arr):
    for i in range(0, len(arr)-1):
        minIndex = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr
