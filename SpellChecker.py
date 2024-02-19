import re
import string

from collections import Counter
import numpy as np

class SpellCHecker(object):

  def __init__(self, corpus_file_path):
    # Initialize the SpellCHecker object with the corpus file path
    with open(corpus_file_path, "r") as file:
      lines = file.readlines()
      words = []
      # Collect all the words from the corpus file
      for line in lines:
        words += re.findall(r'\w+', line.lower())

    # Create a set of all the words in the corpus and their frequency counts
    self.vocabs = set(words)
    self.word_counts = Counter(words)
    total_words = float(sum(self.word_counts.values()))
    # Calculate the probability of each word in the corpus
    self.word_probas = {word: self.word_counts[word] / total_words for word in self.vocabs}

  def first_transformation(self, word):
    #if word is in corpus return word as it is already correct
    if word in self.vocabs:
            return {word}
    # Create a set of all possible first transformations for the given word  add more and correcr cor[us]
     
    characters = string.ascii_lowercase
    #Create a set of all possible splits for the given word
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    #Remove one character from the word
    removes= [char1 + char2[1:] for char1,char2 in splits if char2]
    #Shift adjacent characters by one position
    shifted = [char1[-1] + char2[:-1] + char1[:-1] + char2[-1] for char1, char2 in splits if len(char1) > 0 and len(char2) > 0]
    #Swap adjacent characters
    swaps = [char1 + char2[1] + char2[0] + char2[2:] for char1, char2 in splits if len(char2)>1]
    #Replace a character with every possible lowercase letter
    replaces = [char1 + c + char2[1:] for char1, char2 in splits if char2 for c in characters]
    #Insert every possible lowercase letter at every possible position in the word
    inserts = [char1 + c + char2 for char1, char2 in splits for c in characters] 

    return set(removes + swaps + replaces + inserts + shifted)

  def second_transformation(self, word):
    # Create a set of all possible second transformationsfor the given word usuing the first transformations
    return set(e2 for e1 in self.first_transformation(word) for e2 in self.first_transformation(e1))

  def third_transformation(self, word):
    # Create a set of all possible third transformations for the given word usuing first and second transformations
    level_two_edits = self.second_transformation(word)
    level_three_edits = set(e3 for e2 in level_two_edits for e3 in self.first_transformation(e2))
    return level_three_edits

  def check(self, word):
     
    # create candidate set
    candidates = self.first_transformation(word) or self.second_transformation(word)  or self.third_transformation(word) or [word]
    # return a sorted list of candidate words that are in the vocabulary set based on their probability
    valid_candidates = [w for w in candidates if w in self.vocabs]
    return sorted([(c, self.word_probas[c]) for c in valid_candidates], key=lambda tup: tup[1], reverse=True)



  def correct_text(self,input_file):
    # Correct the text in the input file
    with open(input_file, mode='r', encoding='utf-8-sig') as input_file:
        lines = input_file.readlines()
        corrected_lines = []
        # Loop through each line in the input file
        for line in lines:
          
            words = re.findall(r'\w+', line.lower())
            print(words)
            # Loop through each word in the line
            for word in words:
                
                # Get the most likely candidate for the misspelled word
                #if ther are no suggestions for misplled word you get empty list do justreturn the word
                if  len(self.check(word))==0:
                   corrected_line = "".join(word)

                else:
                  x = self.check(word)[0][0]
                  print(x)
                # Append the corrected word to the corrected line
                  corrected_line = "".join(x)
                  corrected_lines.append(corrected_line)
                #write to output file so the def upload(self)can read the ouput
            with open("./output.txt", "w") as output_file: 
                        for corrected_line in corrected_lines: 
                            output_file.write(corrected_line +" " )
            return x
                   



