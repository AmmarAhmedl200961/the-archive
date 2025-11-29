"""Write a map-reduce to find the average number of songs played daily. Also, add a
combiner. For the above data, the average no of songs would be = (3+4+2+3+1)/5"""
from mrjob.job import MRJob
import csv

class avgsongsperday(MRJob):
    
    def mapper(self, _, line):
        row = next(csv.reader([line]))
        name, date, *songs = row
        yield date, (len(songs), 1)  # Emit a tuple of (number of songs, count of 1)
        
    def combiner(self, date, counts):
        total_songs = 0
        count = 0
        for songs, c in counts: # Iterate over the generator
            total_songs += songs
            count += c
        # we wont be needing the date here, so we can just yield 'daily' as the key
        yield 'daily', (total_songs, count)  # Emit a tuple of (total songs, total count)
        
    def reducer(self, date, counts):
        total_songs = 0
        count = 0
        for songs, c in counts:
            total_songs += songs
            count += c
        yield 'daily', total_songs / count  # Emit the date and the average number of songs
        
if __name__ == '__main__':
    avgsongsperday.run()
