def sort_urls(filename, sort_func):
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

def sort_list(urls):
    # do nothing
    pass

if __name__ == '__main__':
    sort_urls('urls.txt', sort_list)
