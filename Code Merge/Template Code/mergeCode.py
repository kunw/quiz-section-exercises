import sys
import sortUrls
import sort
import getopt


# Validation and normalization function goes here....
def candv(filename):
    return True

def main(argv):
    filename = ''
    arguments = []
    validate = False

    try:
        opts, args = getopt.getopt(argv,"hf:va:",["file=", "valid", "arguments="])
    except getopt.GetoptError:
        print 'Invalid arguments!'
        print 'Usage: mergeCode.py -f <sort file> -v -a <argument1> -a <argument2> ...'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Usage: mergeCode.py -f <sort file> -v -a <argument1> -a <argument2> ...'
            sys.exit()
        elif opt in ("-f", "--file"):
            filename = arg
        elif opt in ("-a", "--arguments"):
            arguments.append(arg)
        elif opt in ("-v", "--valid"):
            validate = True

    if validate:
        valid = candv(filename)

        if valid:
            callSort(filename, arguments)

    else:
        callSort(filename, arguments)


"""
    if filename == '':
        print 'Invalid filename!'
        print 'Usage: mergeCode.py -f <sort file> -v -a <argument1> -a <argument2> ...'
        sys.exit(2)
    else:
        callSort(sortFile
""" 
"""
   if len(argv) < 2:
        print 'Invalid number of arguments!'
        print 'Usage: mergeCode -input [sortFile] -v -arguments [...sortFile args]'
    else:
        sortFile = argv[1]
        arguments = argv[2:]
        callSort(sortFile, arguments)
"""

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
    main(sys.argv[1:])
