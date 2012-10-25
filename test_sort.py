import unittest
from sort import sortfile
from sortalgs import mergesort, quicksort, radixsort, selectionsort

class TestSortFunctions(unittest.TestCase):

    def setUp(self):
        self.list_url = [
            'https://www.google.com',
            'https://github.com/',
            'http://www.google.com',
            'http://www.facebook.com',
            'http://www.facebook.com/groups/405662882833858/407845452615601/?comment_id=407863142613832&notif_t=group_comment_reply',
            'http://www.stackoverflow.com/'
        ]
        self.list_url_sorted = [
            'http://www.facebook.com',
            'http://www.facebook.com/groups/405662882833858/407845452615601/?comment_id=407863142613832&notif_t=group_comment_reply',
            'http://www.google.com',
            'http://www.stackoverflow.com/',
            'https://github.com/',
            'https://www.google.com'
        ]
        self.list_char = [
            'b', 'c', 'a', 'd', 'e', 'f', 'z', 'q'
        ]
        self.list_char_sorted = [
        		'a', 'b', 'c', 'd', 'e', 'f', 'q', 'z'
        ]
        
        self.list_string = [
            'bade', '12zztt5j', 'abc3', 'abc2', 'a9bc2', 'z1jlk', 'acjk', 'qqqqqj', '62lll', '12zzt2kz777', 'bade5j', 'badbz7l'
        ]
        self.list_string_sorted = [
        		'12zzt2kz777', '12zztt5j', '62lll', 'a9bc2', 'abc2', 'abc3', 'acjk', 'badbz7l', 'bade', 'bade5j', 'qqqqqj',  'z1jlk'
        ]
        
        self.list_ascii = [
            'r', 'R', '/', '.', ';', '+', '>', '<', '=', '?', '-', '%', '[', '5'
        ]
        self.list_ascii_sorted = [
        		'%', '+', '-', '.', '/', '5', ';', '<', '=', '>', '?', 'R', '[', 'r',
        ]

    def test_char_quicksort(self):
        self.assertTrue(self.list_char_sorted == quicksort(self.list_char))
        
    def test_char_mergesort(self):
        self.assertTrue(self.list_char_sorted == mergesort(self.list_char))
        
    def test_char_radixsort(self):
        self.assertTrue(self.list_char_sorted == radixsort(self.list_char))
        
    def test_char_selectionsort(self):
        self.assertTrue(self.list_char_sorted == selectionsort(self.list_char))
 
    def test_string_quicksort(self):
        self.assertTrue(self.list_string_sorted == quicksort(self.list_string))
        
    def test_string_mergesort(self):
        self.assertTrue(self.list_string_sorted == mergesort(self.list_string))
        
    def test_string_radixsort(self):
        self.assertTrue(self.list_string_sorted == radixsort(self.list_string))
        
    def test_char_selectionsort(self):
        self.assertTrue(self.list_string_sorted == selectionsort(self.list_string))
 
    def test_empty_quicksort(self):
        self.assertTrue([] == quicksort([]))
        
    def test_empty_mergesort(self):
        self.assertTrue([] == mergesort([]))
        
    def test_empty_radixsort(self):
        self.assertTrue([] == radixsort([]))
        
    def test_empty_selectionsort(self):
        self.assertTrue([] == selectionsort([]))
 
    def test_one_quicksort(self):
        self.assertTrue(['a'] == quicksort(['a']))
        
    def test_one_mergesort(self):
        self.assertTrue(['a'] == mergesort(['a']))
        
    def test_one_radixsort(self):
        self.assertTrue(['a'] == radixsort(['a']))
    
    def test_one_selectionsort(self):
        self.assertTrue(['a'] == selectionsort(['a']))
    
    def test_ascii_quicksort(self):
        self.assertTrue(self.list_ascii_sorted == quicksort(self.list_ascii))
        
    def test_ascii_mergesort(self):
        self.assertTrue(self.list_ascii_sorted == mergesort(self.list_ascii))
        
    def test_ascii_radixsort(self):
        self.assertTrue(self.list_ascii_sorted == radixsort(self.list_ascii))
    
    def test_ascii_selectionsort(self):
        self.assertTrue(self.list_ascii_sorted == selectionsort(self.list_ascii))
        
    def test_url_quicksort(self):
        self.assertTrue(self.list_url_sorted == quicksort(self.list_url))
        
    def test_url_mergesort(self):
        self.assertTrue(self.list_url_sorted == mergesort(self.list_url))
        
    def test_url_radixsort(self):
        self.assertTrue(self.list_url_sorted == radixsort(self.list_url))
        
    def test_url_selectionsort(self):
        self.assertTrue(self.list_url_sorted == selectionsort(self.list_url))
        
if __name__ == '__main__':
    unittest.main()
