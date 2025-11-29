""" \Write a map-reduce to find the names of the users who have played the maximum
number of songs in a day. Also, add a combiner.
"""

from mrjob.job import MRJob
import csv

class maxsong(MRJob):
        
        def mapper(self, _, line):
            row = next(csv.reader([line]))
            name, date, *songs = row
            yield date, (name, len(songs))
            
        def combiner(self, date, counts):
            yield date, max(counts, key=lambda x: x[1])
            
        def reducer(self, date, counts):
            yield date, max(counts, key=lambda x: x[1])
            
if __name__ == '__main__':
    maxsong.run()
