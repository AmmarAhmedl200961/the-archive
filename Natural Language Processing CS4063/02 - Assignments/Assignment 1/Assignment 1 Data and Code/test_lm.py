########################################
## CS447 Natural Language Processing  ##
##           Homework 1               ##
##       Julia Hockenmaier            ##
##       juliahmr@illnois.edu         ##
########################################
##
## Part 1:
## Develop a smoothed n-gram language model and evaluate it on a corpus
##
import os.path
import sys
import random
import math
from operator import itemgetter
from collections import defaultdict
#----------------------------------------
#  Data input 
#----------------------------------------

# Read a text file into a corpus (list of sentences (which in turn are lists of words))
# (taken from nested section of HW0)
def readFileToCorpus(f):
    """ Reads in the text file f which contains one sentence per line.
    """
    if os.path.isfile(f):
        file = open(f, "r") # open the input file in read-only mode
        i = 0 # this is just a counter to keep track of the sentence numbers
        corpus = [] # this will become a list of sentences
        print("Reading file ", f)
        for line in file:
            i += 1
            sentence = line.split() # split the line into a list of words
            #append this lis as an element to the list of sentences
            corpus.append(sentence)
            if i % 1000 == 0:
    	#print a status message: str(i) turns int i into a string
    	#so we can concatenate it
                sys.stderr.write("Reading sentence " + str(i) + "\n")
        #endif
    #endfor
        return corpus
    else:
    #ideally we would throw an exception here, but this will suffice
        print("Error: corpus file ", f, " does not exist")
        sys.exit() # exit the script
    #endif
#enddef

# Preprocess the corpus to help avoid sess the corpus to help avoid sparsity
def preprocess(corpus):
    #find all the rare words
    freqDict = defaultdict(int)
    for sen in corpus:
	    for word in sen:
	       freqDict[word] += 1
	#endfor
    #endfor

    #replace rare words with unk
    for sen in corpus:
        for i in range(0, len(sen)):
            word = sen[i]
            if freqDict[word] < 2:
                sen[i] = UNK
	    #endif
	#endfor
    #endfor

    #bookend the sentences with start and end tokens
    for sen in corpus:
        sen.insert(0, start)
        sen.append(end)
    #endfor
    
    return corpus
#enddef

def preprocessTest(vocab, corpus):
    #replace test words that were unseen in the training with unk
    for sen in corpus:
        for i in range(0, len(sen)):
            word = sen[i]
            if word not in vocab:
                sen[i] = UNK
	    #endif
	#endfor
    #endfor
    
    #bookend the sentences with start and end tokens
    for sen in corpus:
        sen.insert(0, start)
        sen.append(end)
    #endfor

    return corpus
#enddef

# Constants 
UNK = "UNK"     # Unknown word token
start = "<s>"   # Start-of-sentence token
end = "</s>"    # End-of-sentence-token


#--------------------------------------------------------------
# Language models and data structures
#--------------------------------------------------------------

# Parent class for the three language models you need to implement
class LanguageModel:
    # Initialize and train the model (ie, estimate the model's underlying probability
    # distribution from the training corpus)
    def __init__(self, corpus):
        print("""Your task is to implement five kinds of n-gram language models:
      a) an (unsmoothed) unigram model (UnigramModel)
      b) a unigram model smoothed using Laplace smoothing (SmoothedUnigramModel)
      c) an unsmoothed bigram model (BigramModel)
      d) a bigram model smoothed using absolute discounting (SmoothedBigramModelAD)
      e) a bigram model smoothed using kneser-ney smoothing (SmoothedBigramModelKN)
      """)
    #enddef

    # Generate a sentence by drawing words according to the 
    # model's probability distribution
    # Note: think about how to set the length of the sentence 
    #in a principled way
    def generateSentence(self):
        print("Implement the generateSentence method in each subclass")
        return "mary had a little lamb ."
    #emddef

    # Given a sentence (sen), return the probability of 
    # that sentence under the model(it might be quite small, so use log)
    def getSentenceProbability(self, sen):
        print("Implement the getSentenceProbability method in each subclass")
        return 0.0
    #enddef

    # Given a corpus, calculate and return its perplexity 
    #(normalized inverse log probability)
    def getCorpusPerplexity(self, corpus):
        print("Implement the getCorpusPerplexity method")
        return 0.0
    #enddef

    # Given a file (filename) and the number of sentences, generate a list
    # of sentences and write each to file along with its model probability.
    # Note: you shouldn't need to change this method
    def generateSentencesToFile(self, numberOfSentences, filename):
        filePointer = open(filename, 'w+')
        for i in range(0,numberOfSentences):
            sen = self.generateSentence()
            prob = self.getSentenceProbability(sen)

            stringGenerated = str(prob) + " " + " ".join(sen)
            print(stringGenerated, end="\n", file=filePointer)
            
	#endfor
    #enddef
#endclass

# Unigram language model
class UnigramModel(LanguageModel):
    def __init__(self, corpus):
        self.counts = defaultdict(float);
        self.total = 0.0;
        self.train(corpus)

    def train(self, corpus):
        for sen in corpus:
            for word in sen:
                if word == start:
                    continue
                self.counts[word] += 1.0
                self.total += 1.0

    def prob(self, word):
        return self.counts[word] / self.total

    def draw(self):
        rand = random.random()
        for word in self.counts.keys():
            rand -= self.prob(word)
            if rand <= 0.0:
                return word

    def generateSentence(self):
        sent = [start]
        while (1):
            newword = self.draw()
            sent.append(newword)
            if newword == end:
                break

        return sent

    def getSentenceProbability(self, sen):
        raw_result = 0
        for word in sen[1:]:
            raw_result += math.log(self.prob(word))
        return math.exp(raw_result)

    def getSentenceLogProbability(self, sen):
        raw_result = 0
        for word in sen[1:]:
            raw_result += math.log(self.prob(word))
        return raw_result

    def getCorpusPerplexity(self, corpus):
        logsum = 0
        for sen in corpus:
            '''
            tempprob = self.getSentenceProbability(sen)
            if tempprob == 0:
                tempprob = 0
            logsum += math.log(tempprob)
            '''
            logsum += self.getSentenceLogProbability(sen)
        return math.exp(-logsum/self.total)

    #endddef
#endclass

#Smoothed unigram language model (use laplace for smoothing)
class SmoothedUnigramModel(LanguageModel):
    def __init__(self, corpus):
        self.counts = defaultdict(float)
        self.total = 0.0
        self.train(corpus)

    def train(self, corpus):
        for sen in corpus:
            for word in sen:
                if word == start:
                    continue
                self.counts[word] += 1.0
                self.total += 1.0

    def prob(self, word):
        return (self.counts[word] + 1) / (self.total + len(self.counts))

    def draw(self):
        rand = random.random()
        for word in self.counts.keys():
            rand -= self.prob(word)
            if rand <= 0.0:
                return word

    def generateSentence(self):
        sent = [start]
        while (1):
            newword = self.draw()
            sent.append(newword)
            if newword == end:
                break
        return sent

    def getSentenceProbability(self, sen):
        raw_result = 0
        for word in sen[1:]:
            raw_result += math.log(self.prob(word))
        return math.exp(raw_result)

    def getSentenceLogProbability(self, sen):
        raw_result = 0
        for word in sen[1:]:
            raw_result += math.log(self.prob(word))
        return raw_result

    def getCorpusPerplexity(self, corpus):
        logsum = 0
        for sen in corpus:
            #logsum += math.log(self.getSentenceProbability(sen))
            logsum += self.getSentenceLogProbability(sen)
        return math.exp(-logsum/self.total)

    #endddef
#endclass

# Unsmoothed bigram language model
class BigramModel(LanguageModel):
    def __init__(self, corpus):
        self.double_count = defaultdict(float)
        self.single_count = defaultdict(float)
        self.following = defaultdict(set)

        self.total_pair_num = 0
        self.corpus = corpus
        self.train(corpus)
        self.test() #COMMENT THIS LINE BEFORE SUBMISSION

    def train(self, corpus):
        for sen in corpus:
            for i in range(len(sen)):
                if i!= len(sen)-1:
                    self.double_count[(sen[i], sen[i+1])] += 1.0
                    self.following[sen[i]].add(sen[i+1])
                    self.total_pair_num += 1.0
                self.single_count[sen[i]] += 1.0

    def test(self):
        pass

    def prob(self, word, prevword):
        return self.double_count[(prevword, word)]/self.single_count[prevword]

    def draw(self, prevword):
        rand = random.random()
        for word in self.following[prevword]:
            rand -= self.prob(word=word, prevword=prevword)
            if rand <= 0.0:
                return word
        return word

    def generateSentence(self):
        sent = [start]
        lastword = start
        while(1):
            newword = self.draw(lastword)
            sent.append(newword)
            if(newword == end):
                break
            lastword = newword
        return sent

    def getSentenceProbability(self, sen):
        raw_result = 0
        prevword = start
        for word in sen[1:]:
            tempprob = self.prob(word= word, prevword=prevword)
            if tempprob == 0:
                return 0
            raw_result += math.log(tempprob)
            prevword = word
        return math.exp(raw_result)

    def getSentenceLogProbability(self, sen):
        raw_result = 0
        small_positive_value = 0.000000000000000000000000001
        prevword = start
        for word in sen[1:]:
            tempprob = self.prob(word=word, prevword=prevword)
            if tempprob > 0:
                raw_result += math.log(tempprob)
            else:
                raw_result += math.log(small_positive_value)
            prevword = word
        return raw_result

    def getCorpusPerplexity(self, corpus):
        logsum = 0.0
        for sen in corpus:
            #logsum += math.log(self.getSentenceProbability(sen))
            logsum += self.getSentenceLogProbability(sen)
        return math.exp(-logsum / self.total_pair_num)

    #endddef
#endclass

# Smoothed bigram language model (use absolute discounting for smoothing)
class SmoothedBigramModelAD(LanguageModel):
    def __init__(self, corpus):
        self.double_count = defaultdict(float)
        self.single_count = defaultdict(float)
        self.following = defaultdict(set)
        self.number_of_words = 0.0
        self.number_of_words_exclude_start_and_end = 0.0;
        self.size_of_vocab_exclud_start_and_end = 0.0;
        self.pair_once = 0.0
        self.pair_twice = 0.0
        self.D = 0.0
        self.total_pair_sum = 0.0
        self.corpusLen = len(corpus)
        self.corpus = corpus  # REMOVE BEFORE SUBMISSION
        #variables used to calculate the laplace probability
        self.counts = defaultdict(float)

        self.total = 0.0

        self.train(corpus)

        self.test() #REMOVE BEFORE SUBMISSION

    def train(self, corpus):
        for sen in corpus:
            for i in range(len(sen)):
                if i != len(sen) - 1:
                    self.double_count[(sen[i], sen[i + 1])] += 1.0

                    if self.double_count[(sen[i], sen[i+1])] == 1.0:
                        self.pair_once += 1

                    if self.double_count[(sen[i], sen[i+1])] == 2.0:
                        self.pair_once -= 1
                        self.pair_twice += 1

                    if self.double_count[(sen[i], sen[i + 1])] == 3.0:
                        self.pair_twice-=1

                    self.following[sen[i]].add(sen[i + 1])
                    self.total_pair_sum += 1.0

                if i != 0:
                    self.counts[sen[i]] += 1.0
                    self.total += 1.0

                self.single_count[sen[i]] += 1.0
                self.number_of_words += 1.0
                self.number_of_words_exclude_start_and_end += 1.0
            self.number_of_words -= 1.0
            self.number_of_words_exclude_start_and_end -= 2.0

        self.D = self.pair_once / (self.pair_once + 2*self.pair_twice)
        self.size_of_vocab_exclud_start_and_end = len(self.single_count) - 2
        self.count_len = len(self.counts)

    def test(self):
        pass

    def draw(self, prevword):
        rand = random.random()
        for word in self.single_count.keys():
            rand -= self.prob(word=word, prevword=prevword)
            if rand <= 0.0:
                return word

    def laplaceprob(self, word):
        return (self.counts[word] + 1) / (self.total + self.count_len)

    def generateSentence(self):
        sent = [start]
        prevword = start
        while(1):
            newword = self.draw(prevword)
            sent.append(newword)
            if newword == end or not newword:
                break
            prevword = newword
        return sent

    def prob(self, word, prevword):
        part1 = max(self.double_count[(prevword, word)]-self.D,0)/self.single_count[prevword]
        laplaceprob = self.laplaceprob(word=word)
        part2 = self.D * len(self.following[prevword]) * laplaceprob/self.single_count[prevword]
        return part1 + part2

    def getSentenceProbability(self, sen):
        raw_result = 0
        prevword = start
        for word in sen[1:]:
            tempprob = self.prob(word= word, prevword=prevword)
            if tempprob == 0:
                return 0
            raw_result += math.log(tempprob)
            prevword = word
        return math.exp(raw_result)

    def getSentenceLogProbability(self, sen):
        raw_result = 0
        prevword = start
        for word in sen[1:]:
            tempprob = self.prob(word= word, prevword=prevword)
            raw_result += math.log(tempprob)
            prevword = word
        return raw_result

    def getCorpusPerplexity(self, corpus):
        logsum = 0
        for sen in corpus:
            #logsum += math.log(self.getSentenceProbability(sen))
            logsum += self.getSentenceLogProbability(sen)
        return math.exp(-logsum / self.total_pair_sum)

            #endddef
#endclass

# Smoothed bigram language model (use absolute discounting and kneser-ney for smoothing)
class SmoothedBigramModelKN(LanguageModel):

    def __init__(self, corpus):
        self.double_count = defaultdict(float)
        self.double_count = {}
        self.double_count = defaultdict(float)
        self.single_count = defaultdict(float)
        self.following = defaultdict(set)
        self.previous = defaultdict(set)
        self.pair_once = 0.0
        self.pair_twice = 0.0
        self.D = 0.0
        self.total_pair_sum = 0.0
        self.corpusLen = len(corpus)
        self.corpus = corpus  # REMOVE BEFORE SUBMISSION
        self.train(corpus)
        self.test()  # REMOVE BEFORE SUBMISSION

    def train(self, corpus):
        for sen in corpus:
            for i in range(len(sen)):

                if i != len(sen) - 1:
                    #if sen[i] is not the last word
                    self.double_count[(sen[i], sen[i + 1])] += 1.0

                    if self.double_count[(sen[i], sen[i + 1])] == 1.0:
                        self.pair_once += 1

                    if self.double_count[(sen[i], sen[i + 1])] == 2.0:
                        self.pair_once -= 1
                        self.pair_twice += 1

                    if self.double_count[(sen[i], sen[i + 1])] == 3.0:
                        self.pair_twice -= 1

                    self.following[sen[i]].add(sen[i + 1])
                    self.total_pair_sum += 1.0

                if i != 0:
                    #if sen[i] is not the first word
                    self.previous[sen[i]].add(sen[i-1])
                self.single_count[sen[i]] += 1.0

        self.D = self.pair_once / (self.pair_once + 2 * self.pair_twice)
        self.double_count_length = len(self.double_count)

    def test(self):
        pass

    def draw(self, prevword):
        rand = random.random()
        for word in self.single_count.keys():  #???????????
            rand -= self.prob(word=word, prevword=prevword)
            if rand <= 0.0:
                return word

    def generateSentence(self):
        sent = [start]
        prevword = start
        while (1):
            newword = self.draw(prevword)
            sent.append(newword)
            if newword == end:
                break
            prevword = newword
        return sent

    def contprob(self, word):
        return len(self.previous[word])/self.double_count_length
        #return len(self.previous[word]) / 15

    def prob(self, word, prevword):
        part1 = max(self.double_count[(prevword, word)] - self.D, 0) / self.single_count[prevword]
        contprob = self.contprob(word=word)
        part2 = self.D * len(self.following[prevword]) * contprob / self.single_count[prevword]
        return part1 + part2

    def getSentenceProbability(self, sen):
        raw_result = 0
        prevword = start
        for word in sen[1:]:
            tempprob = self.prob(word=word, prevword=prevword)
            if tempprob == 0:
                return 0
            raw_result += math.log(tempprob)
            prevword = word
        return math.exp(raw_result)

    def getSentenceLogProbability(self, sen):
        raw_result = 0
        prevword = start
        for word in sen[1:]:
            tempprob = self.prob(word=word, prevword=prevword)
            raw_result += math.log(tempprob)
            prevword = word
        return raw_result

    def getCorpusPerplexity(self, corpus):
        logsum = 0
        for sen in corpus:
            #logsum += math.log(self.getSentenceProbability(sen))
            logsum += self.getSentenceLogProbability(sen)
        return math.exp(-logsum / self.total_pair_sum)

            # endddef
    #endddef
#endclass

# Sample class for a unsmoothed unigram probability distribution
# Note: 
#       Feel free to use/re-use/modify this class as necessary for your 
#       own code (e.g. converting to log probabilities after training). 
#       This class is intended to help you get started
#       with your implementation of the language models above.
class UnigramDist:
    def __init__(self, corpus):
        self.counts = defaultdict(float)
        self.total = 0.0
        self.train(corpus)
    #endddef

    # Add observed counts from corpus to the distribution
    def train(self, corpus):
        for sen in corpus:
            for word in sen:
                if word == start:
                    continue
                self.counts[word] += 1.0
                self.total += 1.0
            #endfor
        #endfor
    #enddef

    # Returns the probability of word in the distribution
    def prob(self, word):
        return self.counts[word]/self.total
    #enddef

    # Generate a single random word according to the distribution
    def draw(self):
        rand = random.random()
        for word in self.counts.keys():
            rand -= self.prob(word)
            if rand <= 0.0:
                return word
	    #endif
	#endfor
    #enddef
#endclass

#-------------------------------------------
# The main routine
#-------------------------------------------
if __name__ == "__main__":
    #read your corpora
    trainCorpus = readFileToCorpus('train.txt')
    trainCorpus = preprocess(trainCorpus)
    
    posTestCorpus = readFileToCorpus('pos_test.txt')
    negTestCorpus = readFileToCorpus('neg_test.txt')
    
    vocab = set()
    # Please write the code to create the vocab over here before the function preprocessTest
    print("""Task 0: create a vocabulary(collection of word types) for the train corpus""")
    for sen in trainCorpus:
        for token in sen:
            vocab.add(token)

    posTestCorpus = preprocessTest(vocab, posTestCorpus)
    negTestCorpus = preprocessTest(vocab, negTestCorpus)

    # Run sample unigram dist code
    unigramDist = UnigramDist(trainCorpus)
    unigramModel = UnigramModel(trainCorpus)
    smoothedUnigramModel = SmoothedUnigramModel(trainCorpus)
    bigramModel = BigramModel(trainCorpus)
    smoothedBigramModelAD = SmoothedBigramModelAD(trainCorpus)
    smoothedBigramModelKN = SmoothedBigramModelKN(trainCorpus)

    unigramModel.generateSentencesToFile(numberOfSentences=20, filename='unigram_output.txt')
    smoothedUnigramModel.generateSentencesToFile(numberOfSentences=20, filename='smooth_unigram_output.txt')
    bigramModel.generateSentencesToFile(numberOfSentences=20, filename=' bigram_output.txt')
    smoothedBigramModelAD.generateSentencesToFile(numberOfSentences=20, filename='smooth_bigram_ad_output.txt')
    smoothedBigramModelKN.generateSentencesToFile(numberOfSentences=20, filename='and_smooth_bigram_kn_output.txt')
    print("The preplexity of the positive test corpus of the unigram model is", unigramModel.getCorpusPerplexity(posTestCorpus))
    print("The preplexity of the negitive test corpus of the unigram model is", unigramModel.getCorpusPerplexity(negTestCorpus))

    print("The preplexity of the positive test corpus of the smoothed unigram model is", smoothedUnigramModel.getCorpusPerplexity(posTestCorpus))
    print("The preplexity of the negative test corpus of the smoothed unigram model is", smoothedUnigramModel.getCorpusPerplexity(negTestCorpus))
    print('The preplexity of the positive test corpus of the biagram model is', bigramModel.getCorpusPerplexity(posTestCorpus))
    print('The preplexity of the negaive test corpus of thebiagram model is', bigramModel.getCorpusPerplexity(negTestCorpus))
    print("The preplexity of the positive test corpus of the smoothed biagram model AD is,", smoothedBigramModelAD.getCorpusPerplexity(posTestCorpus))
    print("The preplexity of the negative test corpus of the smoothed biagram model AD is,",
          smoothedBigramModelAD.getCorpusPerplexity(negTestCorpus))

    print('The preplexity of the positive test corpus of the smoothed biagram model KN is', smoothedBigramModelKN.getCorpusPerplexity(posTestCorpus))
    print('The preplexity of the negative test corpus of the smoothed biagram model KN is',
          smoothedBigramModelKN.getCorpusPerplexity(negTestCorpus))

    print('Finished')
    print("Sample UnigramDist output:")
    print("Probability of \"vader\": ", unigramDist.prob("vader"))
    print("Probability of \""+UNK+"\": ", unigramDist.prob(UNK))
    print("\"Random\" draw: ", unigramDist.draw())
