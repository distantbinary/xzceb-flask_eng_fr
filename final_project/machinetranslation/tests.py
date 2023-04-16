import unittest
import translator
# from machinetranslation import translator

class TestTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.englishToFrench("Hello"), "Bonjour")
        self.assertEqual(translator.frenchToEnglish("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()
