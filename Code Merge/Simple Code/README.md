## Quiz Section Exercises

#### Overview
Our sorting algorithms:
* Merge sort (O(n log n))
* Quick sort (O(n log n))
* Radix sort (O(n))
* Selection sort (O(n^2))

---

#### Usage
The available sorting algorithms are named:
* mergesort
* quicksort
* radixsort
* selectionsort

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

Replace 'mergesort' in the above examples with any of the other
sorting algorithm names to use the other algorithms.

Output automatically goes to 'sorted_urls.txt'.

---

### Division of Work
How we divided the work:
* One person for each algorithm (4 total)
* One person for input/output
* One person writing tests
* One person creating test cases
