# Invert all the words in Input_File.txt file which contain one or more vowels and write the
# complete content (with inverted and non-inverted words) into another file which will be
# created at run time. For example ‘computer’ will be inverted to ‘retupmoc’.

import re

def invert_word(word):
  return word[::-1]

with open('Input File.txt', 'r') as infile, open('task4.txt', 'w') as outfile:
    for line in infile:
      words = line.split()
      new_line = ""
      for word in words:
        if re.search(r'[aeiouAEIOU]', word):
          new_line += invert_word(word) + " "
        else:
          new_line += word + " "
      outfile.write(new_line + "\n")

