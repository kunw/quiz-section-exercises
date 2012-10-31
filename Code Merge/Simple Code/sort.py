import sys
import sys
from sortalgs import mergesort, quicksort, radixsort, selectionsort, insertionsort, bucketsort, mergesort2, quicksort2

def sortfile(filename, sort_func):
    '''
    Reads in a list of urls from the given filename and passes it to the
    passed sorting function. The sorted urls are then printed to a new file,
    "sorted_urls.txt"
    '''
    # Read in list of urls from file
    url_list = open(filename).readlines()
      
    # Sort urls
    url_list = sort_func(url_list)

    # Print out sorted URLs to file
    f =  open('sorted.txt', 'w')
    for url in url_list:
        f.write(url)

def main(arg):
    if len(arg) != 2:
        print 'Invalid number of arguments!'
        print 'Usage: python sort.py [filename] [sortfunc]'
    else:
        filename = arg[0]
        func = arg[1]
        sortfunc = None
        if func == 'mergesort':
            sortfunc = mergesort
        elif func == 'quicksort':
            sortfunc = quicksort
        elif func == 'radixsort':
            sortfunc = radixsort
        elif func == 'selectionsort':
            sortfunc = selectionsort
        elif func == 'insertionsort':
            sortfunc = insertionsort
        elif func == 'bucketsort':
            sortfunc = bucketsort
        elif func == 'mergesort2':
            sortfunc = mergesort2
        elif func == 'quicksort2':
            sortfunc = quicksort2
        else:
            raise Exception('Invalid sort function: ' + func)
        sortfile(filename, sortfunc)

if __name__ == "__main__":
    main(sys.argv[1:])
