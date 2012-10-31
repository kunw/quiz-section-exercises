import sys
import sortUrls
import sort

def main(argv):
    if len(argv) < 2:
        print 'Invalid number of arguments!'
        print 'Usage: python mergeCode [sortFile] [...sortFile args]'
    else:
        sortFile = argv[1]
        arguments = argv[2:]
        callSort(sortFile, arguments)

def callSort(sortFile, arguments=[]):
    try:
        if sortFile == 'sort.py':
            sort.main(arguments)
        elif sortFile == 'sortUrls.py':
            print(arguments)
            sortUrls.main(arguments)
        else:
            raise Exception('File sorting implementation not included/found.')

    except IOError as e:
        print "Error: File \"" + argv[1] + "\" not found."
    except IndexError as e:
        print errorMessage
    except ValueError as e:
        print errorMessage
    except KeyError as e:
        print errorMessage

if __name__ == "__main__":
    main(sys.argv)
