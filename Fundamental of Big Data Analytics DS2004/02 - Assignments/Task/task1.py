
# file magic to create a file called task1.py
# file twitter-data.txt is of format: date, message, location, metadata
from mrjob.job import MRJob
import re
class MRWordFrequencyCount(MRJob):
    def mapper(self, _, line):
        # Split the line into fields 
        date, message,location,*other_metadata = line.split(',') # Extract the date and message

        date = date.strip()

        message = message.strip() # Extract words from the message
        words = re.findall(r'\w+', message.lower()) # Emit key-value pairs where the key is a composite key consisting of the date and word, 
        # and the value is 1

        for word in words:

            yield (date, word), 1

    def reducer(self, key, values): # Aggregate the counts for each word on each date
        yield key[0], (key[1], sum(values))
        
if __name__ == '__main__':
    MRWordFrequencyCount.run()
