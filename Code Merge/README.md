## Code Merging Exercise

### Note:

For this particular code, no modifications have been made to either the
implementation and usage of EventHub code nor the TileToTheTop code. Each 
code now has a main function defined in addition to the main module. 

### Usage

Example Python script usage:
```python
import mergeCode

filename1 = 'urls1.txt'
filename2 = 'urls2.txt'
mergeCode.main(['sort.py', filename1, 'mergesort'])
mergeCode.main(['sortUrls.py', filename2, 'sortedResults.txt'])
```

Example command line usage:
```
python mergeCode.py sort.py urls1.txt quicksort

python mergeCode.py sortUrls.py urls2.txt sortResults.txt
```

Replace 'sort.py' and 'sortUrls.py' with any other group's main
code that runs the sorting algorithm.

NOTE: LOOK AT OTHER GROUP'S DOCUMENTATION/SPECIFICATION TO PASS CORRECT
      ARGUMENTS INTO FUNCTION.

All arguments needed to run the group's code need to be given to run
correctly. This code only enables other group's code to be linked but doesn't
provide any arguments to make sure the code runs (forces user to give correct
arguments for code to work).
