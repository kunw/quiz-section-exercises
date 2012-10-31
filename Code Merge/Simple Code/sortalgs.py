import random
from heapq import *

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

############################################################

# Mergesort
def mergesort(n):
    if len(n) > 1:
        mid = len(n) // 2
        a = n[mid:]
        b = n[:mid]
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
        if (a[0] < b[0]):
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
    
############################################################
    
# (Modified code taken from http://codehost.wordpress.com/2011/07/22/radix-sort/)
# Radix sort for variable length strings
def radixsort(array):
    if (len(array) <= 1):
        return array
    maxLen = -1
    for string in array: # Find longest string
        strLen = len(string)
        if strLen > maxLen:
            maxLen = strLen
    oa = ord('0') - 1; # First character code
    oz = ord('z') - 1; # Last character code
    n = oz - oa + 2; # Number of buckets (+empty character)
    buckets = [[] for i in range(0, n)] # The buckets
    for position in reversed(range(0, maxLen)):
        for string in array:
            index = 0 # Assume "empty" character
            if position < len(string): # Might be within length
                index = ord(string[position]) - oa
            buckets[index].append(string) # Add to bucket
        del array[:]
        for bucket in buckets: # Reassemble array in new order
            array.extend(bucket)
            del bucket[:]
    return array

############################################################

# Selection sort algorithm
def selectionsort(arr):
    for i in range(0, len(arr)-1):
        minIndex = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr

"""
Comparison functions

Arguments:
    a - first element to compare
    b - second element to compare
Returns:
    negative integer if the first precedes the second
    0 if both arguments have equal ordering
    positive integer if the first succeeds the second

"""

# default to sort by length
def default_cmp(a, b):
    return len(a) - len(b)


"""

Sorting functions

Arguments:
    list - list of elements (url strings)
    cmp  - comparison function
Returns:
    sorted list of elements
    
"""

def quicksort2(list, cmp=default_cmp):
    return qsort2(list[:], cmp)

def qsort2(list, cmp):
    if list == []:
        return list
    else:
        pivot_ndx = random.choice(range(len(list)))
        pivot = list.pop(pivot_ndx)
        left = [x for x in list if cmp(x, pivot) < 0]
        right = [x for x in list if cmp(x, pivot) >= 0]
        return qsort2(left, cmp) + [pivot] + qsort2(right, cmp)

def insertionsort(list, cmp=default_cmp):
    for i in range(1, len(list)):
        save = list[i]
        j = i
        while j > 0 and cmp(list[j - 1], save) > 0:
            list[j] = list[j - 1]
            j -= 1
        list[j] = save
    return list

def mergesort2(list, cmp=default_cmp):
    size = len(list)
    if (size <= 1):
        return list
    left = mergesort2(list[0 : size/2], cmp)
    right = mergesort2(list[size/2 : size], cmp)
    return merge2(left, right, cmp)

def merge2(left, right, cmp):
    result = []
    while (len(left) > 0 or len(right) > 0):
        # both non empty
        if (len(left) > 0 and len(right) > 0):
            c = cmp(left[0], right[0])
            if (c <= 0):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # right is empty
        elif (len(left) > 0):
            result.append(left.pop(0))
        # left is empty
        else:
            result.append(right.pop(0))
    return result

def msvalue(n):
    '''
    Returns the most significant value of n, i.e. n rounded
    down to the nearest significant digit.

    So msvalue(1)   -> 1
       msvalue(25)  -> 10
       msvalue(987) -> 100
    '''
    if n < 10:
        return 1
    else:
        return 10 * msvalue(n / 10)

def bucketsort(list, cmp=default_cmp):
    '''
    Recursively performs bucket sort on the list
    of strings, using their lengths to index
    them.
    '''

    # Pre-parse the length of each string in the list
    # so that we can find the min and max with which to set
    # up the buckets.
    len_list = []
    max_val = 0
    min_val = sys.maxint
    for i in range(len(list)):
        length = len(list[i])
        len_list.append((length, list[i])) # store list item as tuple (length, item)
        if length > max_val:
            max_val = length
        if length < min_val:
            min_val = length

    # Range of values that each bucket holds.
    bucket_size = msvalue(max_val - min_val)

    # Set up the empty buckets.
    num_buckets = (max_val / bucket_size) - (min_val / bucket_size)
    bucket_list = []
    for i in range(num_buckets + 1):
        bucket_list.append([])

    # Index the list elements into their respective buckets.
    n = len(list)
    for i in range(n):
        # Items are indexed by rounding down to the nearest bucket.
        index = (len_list[i][0] / bucket_size) - (min_val / bucket_size)

        bucket_list[index].append(len_list[i][1])

    # Sort the buckets. If all elements indexed
    # to the same bucket, use another sorting
    # algorithm to perform the final sort on
    # that bucket.
    for i in range(len(bucket_list)):
        if len(bucket_list[i]) > 0:
            if len(bucket_list[i]) == len(list):
                bucket_list[i] = insertionsort(bucket_list[i], cmp)
            else:
                bucket_list[i] = bucketsort(bucket_list[i])

    # Concatenate all of the sorted buckets
    ret_val = []
    for i in range(len(bucket_list)):
        ret_val += bucket_list[i]

    return ret_val

