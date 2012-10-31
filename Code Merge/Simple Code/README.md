## Quiz Section Exercises

#### Overview

This code works similar to the first exercise (see quiz-section-exercise README for details)
except that the code runs with the four algorithms of another group. The following algorithms
are available to choose for running:

* Merge sort (O(n log n))
* Quick sort (O(n log n))
* Radix sort (O(n))
* Selection sort (O(n^2))
* Insertion sort (O(n^2))
* Bucket sort (O(n))

---

#### Usage
The available sorting algorithms are named:
* mergesort
* quicksort
* radixsort
* selectionsort
* mergesort2
* quicksort2
* insertionsort
* bucketsort

Example Python script usage:
```python
from sort import sortfile
from sortalgs import mergesort, mergesort2

filename = 'urls.txt'
sortfile(filename, mergesort)

sortfile(filename, mergesort2)
```

Example command line usage:
```
python sort.py urls.txt quicksort2
```

Replace 'mergesort' in the above examples with any of the other
sorting algorithm names to use the other algorithms.

Output automatically goes to 'sorted_urls.txt'.

---
