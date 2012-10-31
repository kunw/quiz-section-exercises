## Code Merging Exercise

### Code Merge Design

For this particular code, no modifications have been made to either the
implementation and usage of EventHub code nor the TileToTheTop code. Each 
code now has a main function defined in addition to the main module.

Thus, running the code is as easy as replacing 'sort.py' and 'sortUrls.py' 
with any other group's main code that runs the sorting algorithm.


### Notes

* **LOOK AT OTHER GROUP'S DOCUMENTATION/SPECIFICATION TO PASS CORRECT ARGUMENTS INTO FUNCTION!!!!**

All arguments needed to run the group's code need to be given to run
correctly. This code only enables other group's code to be linked but doesn't
provide any arguments to make sure the code runs (forces user to give correct
arguments for code to work).

* **ANY ADDITIONAL SORTING MODULES NEEDS A MAIN FUNCTION AND HAS TO BE INSERTED INTO THE CALLSORT FUCNCTION!!!**

Because the mergeCode module directly calls any additional sorting module directly, it is
required that the sorting module to be added has a main method defined and can be called
(that matches what happens when the code is run at the command line).

* **THERE CANNOT BE ANY SORTING FILES THAT HAVE THE SAME NAME!!!**

Because the module knows which code to run, it requires that no two files have the same
name. However, checking is just as simple as making sure your file doesn't match any other
file names defined in the callSort function (when it makes the checks).


### Usage

Example Python script usage:
```python
import mergeCode

file1 = 'sort.py'
inputfile1 = 'urls1.txt'
sortingAlg = 'mergesort'

file2 = 'sortUrls.py'
inputfile2 = 'urls2.txt'
outputfile = 'sorted.txt'

mergeCode.main(file1, [inputfile1, sortingAlg])
mergeCode.main(file2, [inputfile2, outputfile])
```

Example command line usage:
```
python mergeCode.py sort.py urls1.txt quicksort

python mergeCode.py sortUrls.py urls2.txt sortResults.txt
```

