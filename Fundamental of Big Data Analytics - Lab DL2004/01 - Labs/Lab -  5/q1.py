# Question 1
# Write a Map Reduce algorithm to find the number of times a student accessed his each class on google 
# classroom during year 2020. You have to provide the pseudo-code for Mapper, Reducer and Combiner.
# You can use associative memory (array) in Mapper to make  your program efficient.
from mrjob.job import MRJob
import re

# regex for roll number
reg_roll = re.compile(r'L20-\d{4}')
# regex for class
reg_class = re.compile(r'Course:\w+')
# regex for accessed
reg_accessed = re.compile(r'Accessed:.*')

class timesaccessed(MRJob):
    def mapper(self, _, line):
        student = reg_roll.findall(line)[0]
        course = reg_class.findall(line)[0].split(':')[1]
        
        yield (student, course), 1
            
    def combiner(self, key, values):
        yield (key, sum(values))

    def reducer(self, key, values):
        yield (key, sum(values))

if __name__ == '__main__':
    timesaccessed.run()
