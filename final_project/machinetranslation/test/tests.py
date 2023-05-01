import unittest
import sys
sys.path.append('./')
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
         self.assertEqual(englishToFrench('Hello'), 'Bonjour')
         self.assertEqual(englishToFrench(''), '')
         self.assertEqual(englishToFrench(), '')


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
         self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
         self.assertEqual(frenchToEnglish(''), '')
         self.assertEqual(frenchToEnglish(), '')


unittest.main()