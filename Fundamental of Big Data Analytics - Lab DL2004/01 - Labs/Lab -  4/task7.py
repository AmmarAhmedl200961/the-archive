"""Write a map-reduce to find the names of the users who have played the maximum
number of songs up till now. Also, add a combiner."""
from mrjob.job import MRJob
import csv

class maxsongofuser(MRJob):
        
        def mapper(self, _, line):
            row = next(csv.reader([line]))
            name, date, *songs = row
            yield name, len(songs)
            
        def combiner(self, name, counts):
            yield name, max(counts) # Emit the name and the maximum count
            
        def reducer(self, name, counts):
            yield name, max(counts) # Emit the name and the maximum count
            
if __name__ == '__main__':
    maxsongofuser.run()
