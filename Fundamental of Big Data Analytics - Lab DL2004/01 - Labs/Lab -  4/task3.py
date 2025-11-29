"""Write a map-reduce job to list the number of songs played by each user up till now.
Also, add a combiner."""
from mrjob.job import MRJob
import csv

class songcount(MRJob):
        
        def mapper(self, _, line):
            row = next(csv.reader([line]))
            name, date, *songs = row
            yield name, len(songs)
            
        def combiner(self, name, counts):
            yield name, sum(counts)
            
        def reducer(self, name, counts):
            yield name, sum(counts)
            
if __name__ == '__main__':
    songcount.run()
