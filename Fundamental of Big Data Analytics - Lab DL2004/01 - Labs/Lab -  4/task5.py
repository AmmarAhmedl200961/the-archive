"""Write a map-reduce to find the number of times each song was played. Also, add a
combiner."""
import csv
from mrjob.job import MRJob

class countsong(MRJob):
    def mapper(self, _, line):
        row = next(csv.reader([line]))
        name, date, *songs = row
        for song in songs:
            yield song, 1
            
    def combiner(self, song, counts):
        yield song, sum(counts)
        
    def reducer(self, song, counts):
        yield song, sum(counts)
        
if __name__ == '__main__':
    countsong.run()
