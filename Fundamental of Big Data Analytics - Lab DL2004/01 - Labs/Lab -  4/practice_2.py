"""count all words of length 5 from a text file and display them on a screeen using mapper and reducer"""
from mrjob.job import MRJob
import re
WORD_RE = re.compile(r"[\w']+")

class MRWordFrequencyCount(MRJob):
        
            def mapper(self, _, line):
                for word in WORD_RE.findall(line):
                    if len(word) == 5:
                        yield word.lower(), 1
        
            def reducer(self, key, values):
                yield key, sum(values)
                
if __name__ == '__main__':
    MRWordFrequencyCount.run()
