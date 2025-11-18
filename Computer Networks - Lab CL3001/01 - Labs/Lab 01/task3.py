# Write non-alphabet words (non-alphabet word is the one in which all letters are non-
# alphabet e.g., “a#$2#” is not non-alphabet word but “$%^&amp;#32” is a non-alphabet word)
# from the Input_File.txt file into another text file which will be created at run-time.

import re

# Write only the non-alphabet words to another file
with open('Input File.txt', 'r') as infile, open('task3.txt', 'w') as outfile:
  for line in infile:
      words = line.split()
      for word in words:
          if re.fullmatch(r'[^a-zA-Z]+', word):  # Check if the word contains only non-alphabet characters
              outfile.write(word + ' ')
