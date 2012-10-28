import sys
import sortUrls
import sort

def main(arg):
    if len(arg) < 1:
        print 'Invalid number of arguments!'
        print 'Usage: python mergeCode [sortFile] [...sortFile args]'
    else:
        sortFile = arg[0]

        if sortFile == 'sort.py':
            sort.main(arg)
        elif sortFile == 'sortUrls.py':
            sortUrls.main(arg)
        else:
            raise Exception('File sorting implementation not included/found.')

if __name__ == "__main__":
    main(sys.argv[1:])
