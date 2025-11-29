# in this file i have ran task1 as well as setup MRjob

# import pip

# pip upgrade pip
# pip.main(["install", "--upgrade", "pip"])
# pip.main(["install", "MRjob"])
# pip.main(['install', 'kaggle'])

import mrjob
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFrequencyCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_find_total_wordcount)
        ]

    def mapper_get_words(self, _, line):
        # split the line into words
        date, message, location = line.split(',', 2)
        words = WORD_RE.findall(message)
        for word in words:
            yield (date, word.lower()), 1

    def reducer_count_words(self, word, counts):
        yield word, sum(counts)

    def reducer_find_total_wordcount(self, word, counts):
        yield word[0], (word[1], sum(counts))

if __name__ == '__main__':
    MRWordFrequencyCount.run()
# task will be run as: 'python task1.py twitter_data.txt > task1.txt'
