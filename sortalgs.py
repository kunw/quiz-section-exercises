# Quicksort routine for given collection of elements.

# Simple version defined in wikipedia (uses O(n) memory)
def quicksort(elements):
    # If one or zero elements, then just return (technically already sorted)
    if (len(elements) <= 1):
        return elements
    else:
        # Choose pivot and then create lists containing elements that are
        # less than and greater than the pivot element.
        pivot = elements[len(elements) / 2]
        left = []
        right = []

        for i in range(len(elements)):
            if (i != len(elements)/2):
                if (elements[i] <= pivot):
                    left.append(elements[i])
                else:
                    right.append(elements[i])

        # Now just recursively call quicksort on the left & right lists and combine
        # at the end with the pivot element.
        return quicksort(left) + [pivot] + quicksort(right)


# Mergesort
def mergesort(n):
    if len(n) > 1:
        mid = len(n) // 2
        a = n[:mid]
        b = n[mid:]
        if len(a) > 1:
            a = mergesort(a)
        if len(b) > 1:
                b = mergesort(b)
        return merge(a, b)
    else:
            return n 
   
def merge(a, b):
    result = []
    while a and b:
        if cmp(a[0],b[0])>= 0:
        #if a[0] >= b[0]:
            result.append(a[0])
            a = a[1:]
        else:
            result.append(b[0])
            b = b[1:]
    if a:
        result.extend(a)
    else:
        result.extend(b)
    return result


if __name__ == '__main__':
    #Example usage:
    x = mergesort(["a","A","dl","b","dL","q","dl","z"])
    #x = mergesort([5, 6, 1, 7, 8, 9, 2, 10, 4, 3])
    x.reverse() #the numbers are in descending order by default
    print x
    #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
