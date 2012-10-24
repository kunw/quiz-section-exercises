def sortUrls(filename, sort_func):
  # Read in list of urls from file
  url_list = open(filename).readlines()
  
  # Sort urls
  #url_list = sort_func(url_list)
  sort_func(url_list)

  # Print out sorted URLs to file
  f =  open('sorted_urls.txt', 'w')
  for url in url_list:
    f.write(url)

def sortList(urls):
  # do nothing
  pass

if __name__ == '__main__':
  sortUrls('urls.txt', sortList)
