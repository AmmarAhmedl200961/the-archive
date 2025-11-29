"""Write a map-reduce to find the names of the users who have played the maximum
number of songs in a day. Also, add a combiner."""

from mrjob.job import MRJob
import csv

class maxsong(MRJob):
        
        def mapper(self, _, line):
            row = next(csv.reader([line]))
            name, date, *songs = row
            yield date, (name, len(songs)) # Emit a tuple of (name, number of songs)
            
        def combiner(self, date, counts):
            # get the name, count tuple with the maximum count
            # lambda x: x[1] is a function that returns the second element of a tuple, which is the count
            yield date, max(counts, key=lambda x: x[1]) # Emit the date and the tuple with the maximum count
            
        def reducer(self, date, counts):
            yield date, max(counts, key=lambda x: x[1]) # Emit the date and the tuple with the maximum count
            
if __name__ == '__main__':
    maxsong.run()
