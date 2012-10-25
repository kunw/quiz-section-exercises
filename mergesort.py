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
