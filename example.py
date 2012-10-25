from sort import sortfile
from sortalgs import mergesort, quicksort

filename = 'urls.txt'
sortfile(filename, mergesort)
sortfile(filename, quicksort)
