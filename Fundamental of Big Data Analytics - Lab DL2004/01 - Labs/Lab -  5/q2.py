# Question 2: For each course output the number of distinct students who have accessed the course
# classroom Write an efficient MapReduce algorithm to perform above task.

# Output:
# BigData 1
# DataMining 2

from mrjob.job import MRJob
import re

# regex for roll number
reg_roll = re.compile(r'L20-\d{4}')
# regex for class
reg_class = re.compile(r'Course:\w+')

class distinctstudents(MRJob):
    def mapper(self, _, line):
        student = reg_roll.findall(line)[0]
        course = reg_class.findall(line)[0].split(':')[1]
        
        yield course, student
            
    def reducer(self, key, values):
        # values are incoming students, get the distinct count
        yield key, len(set(values))
        
if __name__ == '__main__':
    distinctstudents.run()
