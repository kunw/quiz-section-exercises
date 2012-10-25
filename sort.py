import sys
from sortalgs import mergesort, quicksort

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
    f =  open('sorted_urls.txt', 'w')
    for url in url_list:
        f.write(url)

if __name__ == "__main__":
    arg = sys.argv
    if len(arg) != 3:
        print 'Invalid number of arguments!'
        print 'Usage: python sort.py [filename] [sortfunc]'
    else:
        filename = arg[1]
        func = arg[2]
        sortfunc = None
        if func == 'mergesort':
            sortfunc = mergesort
        elif func == 'quicksort':
            sortfunc = quicksort
        else:
            raise Exception('Invalid sort function: ' + func)
        sortfile(filename, sortfunc)
