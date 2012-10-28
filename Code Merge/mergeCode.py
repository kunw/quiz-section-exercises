import sys
import sortUrls
import sort

if __name__ == "__main__":
    arg = sys.argv
    if len(arg) < 2:
        print 'Invalid number of arguments!'
        print 'Usage: python testMerge [sortFile] [...sortFile args]'
    else:
        sortFile = arg[1]

        if sortFile == 'sort.py':
            sort.main(arg[1:])
        elif sortFile == 'sortUrls.py':
            sortUrls.main(arg[1:])
        else:
            raise Exception('Invalid file choice.')

