import time
from SpellChecker import SpellCHecker


class TestSpellChecker:

    def setUp(self):
        self.spellchecker = SpellCHecker("./irish.txt")
        print("corrected_text)")

    def test_my_function(self):
        start_time = time.time()
        # code to be timed goes here
        with open("inputtt.txt", mode='w', encoding='utf-8-sig') as input_file:
            input_file.write("freagr freagr freagr freagr freagr freagr freagr freagr freagr freagr freagr freagr freagr freagr")
        # Call the correct_text method on the input file
        self.spellchecker.correct_text("inputt.txt")
        # Read the output file and check if it has the corrected words
        with open("output.txt", mode='r', encoding='utf-8-sig') as output_file:
            corrected_text = output_file.read()
            print(corrected_text)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")