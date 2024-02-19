import unittest
from SpellChecker import SpellCHecker

class TestSpellChecker(unittest.TestCase):
     #creates an instance of the SpellChecker class
    def setUp(self):
        self.spellchecker = SpellCHecker("./irish.txt")
        

    def test_spell_check_correct_word(self):
        # Test correct word is not flagged
        #enter correct spellling word,test passes if correctly spelled word is not flagged as false 
        result = self.spellchecker.check("freagra")
        #print(result)
        self.assertTrue(result)

    def test_spell_check_incorrect_word(self):
        # Test if word is corrected
        #it is true of the word has been translated correctly
        with open("inputt.txt", mode='w', encoding='utf-8-sig') as input_file:
            input_file.write("freagr")
        # Call the correct_text method on the input file
        self.spellchecker.correct_text("inputt.txt")
        # Read the output file and check if it has the corrected words
        with open("output.txt", mode='r', encoding='utf-8-sig') as output_file:
            corrected_text = output_file.read()
            self.assertIn("freagra", corrected_text)

    def test_spell_check_capitalization(self):
        # Test that correct_text method corrects the text in the input file
        # Create an input file with misspelled words
        with open("inputt.txt", mode='w', encoding='utf-8-sig') as input_file:
            input_file.write("Binte")
        # Call the correct_text method on the input file
        self.spellchecker.correct_text("inputt.txt")
        # Read the output file and check if it has the corrected words
        with open("output.txt", mode='r', encoding='utf-8-sig') as output_file:
            corrected_text = output_file.read()
            self.assertIn("bainte", corrected_text)
            
        

    def test_spell_check_capitalization(self):
        # Test that correct_text method corrects the text in the input file
        # Create an input file with misspelled words
        with open("inputt.txt", mode='w', encoding='utf-8-sig') as input_file:
            input_file.write("Binte.")
        # Call the correct_text method on the input file
        self.spellchecker.correct_text("inputt.txt")
        # Read the output file and check if it has the corrected words
        with open("output.txt", mode='r', encoding='utf-8-sig') as output_file:
            corrected_text = output_file.read()
            self.assertIn("bainte", corrected_text)
 
      


if __name__ == '__main__':
    unittest.main()
