from mrjob.job import MRJob

class MRWordCount(MRJob):

    def mapper(self, _, line):
        year, word_count = line.split('\t')
        word, count = eval(word_count)
        yield word, count

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    MRWordCount.run()

# task will be run as: 'python task2.py task1.txt > task2.txt'
