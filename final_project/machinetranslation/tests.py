import unittest 

from translator import EnglishToFrench, FrenchToEnglish

class TestLanguage(unittest.TestCase):
    def testenglish_to_french(self):
        self.assertNotEqual(EnglishToFrench('Hello'),'Bonjur')
        self.assertNotEqual(EnglishToFrench('Hello'),'Hello')
        self.assertNotEqual(EnglishToFrench(' '),'Bonjur')
        self.assertNotEqual(EnglishToFrench(0),0)

    def testfrench_to_english(self):
        self.assertNotEqual(FrenchToEnglish('Bonjur'),'Hello')
        self.assertNotEqual(FrenchToEnglish('Bonjur'),'Bonjur')
        self.assertNotEqual(FrenchToEnglish(' '),'Hello')
        self.assertNotEqual(FrenchToEnglish(0),0)

unittest.main()