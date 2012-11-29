from urlparse import urlparse
import re
def validateUrl(url):
    #contains only valid characters
    #if re.match("^[A-Za-z0-9-._~:/?#[]@]*$", my_little_string):
    #parse url
    o = urlparse(url)
    #scheme is valid
    if(o.scheme=='' or (o.scheme.lower() != 'http' and o.scheme.lower() != 'https')):
        return False;
    #domain is valid
    if(o.netloc==''):
        return False
    return True
