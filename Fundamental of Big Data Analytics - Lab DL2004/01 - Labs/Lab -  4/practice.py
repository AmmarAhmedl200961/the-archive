"""" this job will display how many words start with each alphabet in a text file"""
from mrjob.job import MRJob
import re
WORD_RE = re.compile(r"[\w']+")

class MRWordFrequencyCount(MRJob):
    
        def mapper(self, _, line):
            for word in WORD_RE.findall(line):
                yield word.lower()[0], 1
    
        def reducer(self, key, values):
            yield key, sum(values)
            
if __name__ == '__main__':
    MRWordFrequencyCount.run()
