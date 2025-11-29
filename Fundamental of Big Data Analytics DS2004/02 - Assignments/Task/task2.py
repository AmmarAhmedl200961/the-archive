from mrjob.job import MRJob

class MRTotalWordCount(MRJob):
    def mapper(self, _, line):
        _, word_count = line.split('\t')
        word, count = eval(word_count)
        yield word, int(count)

    def reducer(self, key, counts):
        yield key, sum(counts)

if __name__ == '__main__':
    MRTotalWordCount.run()
