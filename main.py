
# Read in URLs from file
urls = open('urls.txt').readlines()

# Sort URLs
# TODO: need to have sorting functions implemented first

# Print out sorted URLs to file
f =  open('sorted_urls.txt', 'w')
for url in urls:
  f.write(url)

