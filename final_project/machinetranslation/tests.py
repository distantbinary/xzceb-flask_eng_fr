import unittest
import translator
# from machinetranslation import translator

class TestTranslator(unittest.TestCase):
    def test_eng_to_fr(self):
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(translator.english_to_french("Hello"), "Hello")

    def test_fr_to_eng(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(translator.french_to_english("Bonjour"), "Bonjour")

if __name__ == '__main__':
    unittest.main()
