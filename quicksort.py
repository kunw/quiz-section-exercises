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
