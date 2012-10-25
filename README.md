### Quiz Section Exercises

Our sorting algorithms:
* Merge sort (O(n log n))
* Quick sort (O(n log n))
* Radix sort (O(n))
* ??? (O(n^2))

The available sorting algorithms are named:
* mergesort
* quicksort
* radixsort
* ???

Example Python script usage:
```python
from sort import sortfile
from sortalgs import mergesort

filename = 'urls.txt'
sortfile(filename, mergesort)
```

Example command line usage:
```
python sort.py urls.txt quicksort
```

Output automatically goes to 'sorted_urls.txt'.

How we divided the work:
* One person for each algorithm (4 total)
* One person for input/output
* One person writing tests
* One person creating test cases
