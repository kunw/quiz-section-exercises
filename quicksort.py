# Quicksort routine for given collection of elements.

# Simple version defined in wikipedia (uses O(n) memory)
def quicksort(elements):
    # If one or zero elements, then just return (technically already sorted)
    if (elements.getNumElements() <= 1):
        return elements
    else:
        # Choose pivot and then create lists containing elements that are
        # less than and greater than the pivot element.
        pivot = elements.getNumElements() / 2
        left = []
        right = []
        for element in elements:
            if element <= pivot:
                left.append(len(left), element)
            else:
                right.append(len(right), element)

        # Now just recursively call quicksort on the left & right lists and combine
        # at the end with the pivot element.
        return quicksort(left) + [pivot] + quicksort(right)


