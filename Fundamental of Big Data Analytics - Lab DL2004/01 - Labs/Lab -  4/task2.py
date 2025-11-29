"""Write a map-only job to list the name of users, the date, and the number of songs played
on that day."""
from mrjob.job import MRJob
import csv
class userinfo(MRJob):
    
    def mapper(self, _, line):
        row = next(csv.reader([line]))
        name, date, *songs = row
        yield name, (date, len(songs))
        
if __name__ == '__main__':
    userinfo.run()
