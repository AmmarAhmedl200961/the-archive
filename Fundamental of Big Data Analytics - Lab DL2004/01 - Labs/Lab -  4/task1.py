"""Write a map-only job to list the name of users who have played more than 5 songs in a
day"""
from mrjob.job import MRJob
import csv
class songcount(MRJob):
    
    def mapper(self, _, line):
        row = next(csv.reader([line])) # convert the line into a csv row using csv.reader
                                       # and then convert it into a list using next() iterator
        name, date, *songs = row
        if len(songs) > 5:
            yield name, 1
     
if __name__ == '__main__':
    songcount.run()
