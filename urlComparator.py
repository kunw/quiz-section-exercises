from urlCanonicalizer import canonicalizeUrl
def compareUrl(url1, url2):
    url1 = canonicalizeUrl(url1)
    url2 = canonicalizeUrl(url2)
    if(url1==url2):
        return 0
    elif(url1<url2):
        return -1
    else:
        return 1
        
def checkUnique_original(theUrl, filename):
    url_list = open(filename).readlines()
    count=0
    for url in url_list:
        if url=='':
            continue
        if (theUrl==url):
            count+=1
    if(count>1):
        return False
    else:
        return True
        
def checkUnique_canonicalized(theUrl, filename):
    url_list = open(filename).readlines()
    count=0
    for url in url_list:
        if url=='':
            continue
        if (compareUrl(theUrl, url)==0):
            count+=1
    if(count>1):
        return False
    else:
        return True
