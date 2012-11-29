from urlparse import urlparse
import re
def validateUrl(url):
    #contains only valid characters
    #if re.match("^[A-Za-z0-9-._~:/?#[]@]*$", url):
    #parse url
    o = urlparse(url)
    #scheme is valid
    if(o.scheme==''):
        return False;
    #domain is valid
    if(o.netloc==''):
        return False
    return True
