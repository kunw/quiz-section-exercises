import sys
from urlValidator import validateUrl
from urlCanonicalizer import canonicalizeUrl
from urlComparator import checkUnique_original, checkUnique_canonicalized

def urlFileCanonicalizationEngine(filename):
    
    # Read in list of urls from file
    url_list = open(filename).readlines()
    
    # Process urls
    for url in url_list:
        if url=='':
            continue
        print 'Source: ' + url.rstrip('\n')
        isValid = validateUrl(url)
        print 'Valid: ' + str(isValid).lower()
        if not isValid:
            continue
        canonicalizedUrl = canonicalizeUrl(url)
        print 'Canonical: '+canonicalizedUrl
        print 'Source unique: '+str(checkUnique_original(url, filename))
        print 'Canonicalized URL unique: '+str(checkUnique_canonicalized(url, filename))

if __name__ == "__main__":
    arg = sys.argv
    if len(arg) != 2:
        print 'Invalid number of arguments!'
        print 'Usage: python urlFileCanonicalizer.py [filename]'
    else:
        filename = arg[1]
        urlFileCanonicalizationEngine(filename)
