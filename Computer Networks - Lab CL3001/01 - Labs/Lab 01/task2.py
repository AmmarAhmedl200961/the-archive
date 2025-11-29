# Write only the integers from the Input_File.txt file to another file which will be created at runtime.

import re
'''
Reads the text file Input_File.txt and extracts only integers.
Then writes these integers to a newly created file named Output_File.txt
'''
with open('Input File.txt', 'r') as infile, open('Output File.txt', 'w') as outfile:
  file_content = infile.read()
  integers = re.findall(r'\b\d+\b', file_content) # Find all integers in the file
  for num in integers:
    outfile.write(num + ' ') # Write each integer to the output file

