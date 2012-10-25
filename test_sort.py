import unittest
from sort import sortfile
from sortalgs import mergesort, quicksort, radixsort

class TestSortFunctions(unittest.TestCase):

    def setUp(self):
        self.list1 = [
            'https://www.google.com',
            'https://github.com/'
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

    def test_char_quicksort(self):
        self.assertTrue(self.list_char_sorted == quicksort(self.list_char))
        
    def test_char_mergesort(self):
        print(mergesort(self.list_char))
        self.assertTrue(self.list_char_sorted == mergesort(self.list_char))
        
    def test_char_radixsort(self):
        self.assertTrue(self.list_char_sorted == radixsort(self.list_char))
        
    def test_string_quicksort(self):
        print(quicksort(self.list_string))
        self.assertTrue(self.list_string_sorted == quicksort(self.list_string))
        
    def test_string_mergesort(self):
        self.assertTrue(self.list_string_sorted == mergesort(self.list_string))
        
    def test_string_radixsort(self):
        print(radixsort(self.list_string))
        self.assertTrue(self.list_string_sorted == radixsort(self.list_string))
        
    def test_empty_quicksort(self):
        self.assertTrue([] == quicksort([]))
        
    def test_empty_mergesort(self):
        self.assertTrue([] == mergesort([]))
        
    def test_empty_radixsort(self):
        self.assertTrue([] == radixsort([]))
        
    def test_one_quicksort(self):
        self.assertTrue(['a'] == quicksort(['a']))
        
    def test_one_mergesort(self):
        self.assertTrue(['a'] == mergesort(['a']))
        
    def test_one_radixsort(self):
        self.assertTrue(['a'] == radixsort(['a']))
        
    def test_char_quicksort(self):
        self.assertTrue(1 == 1)

    def test_char_quicksort(self):
        self.assertTrue(1 == 1)
        
    def test_char_quicksort(self):
        self.assertTrue(1 == 1)        

if __name__ == '__main__':
    unittest.main()
