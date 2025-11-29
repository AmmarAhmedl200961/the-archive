##
import os.path
import sys
import random
import math
from operator import itemgetter
from collections import defaultdict
import pickle
import numpy as np

# ----------------------------------------
#  Data input
# ----------------------------------------


# Read a text file into a corpus (list of sentences (which in turn are lists of words))
# (taken from nested section of HW0)
def readFileToCorpus(f):
    """Reads in the text file f which contains one sentence per line."""
    if os.path.isfile(f):
        file = open(f, "r")  # open the input file in read-only mode
        i = 0  # this is just a counter to keep track of the sentence numbers
        corpus = []  # this will become a list of sentences
        print("Reading file ", f)
        for line in file:
            i += 1
            sentence = line.split()  # split the line into a list of words
            # append this lis as an element to the list of sentences
            corpus.append(sentence)
            if i % 1000 == 0:
                # print a status message: str(i) turns int i into a string
                # so we can concatenate it
                sys.stderr.write("Reading sentence " + str(i) + "\n")
        # endif
        # endfor
        return corpus
    else:
        # ideally we would throw an exception here, but this will suffice
        print("Error: corpus file ", f, " does not exist")
        sys.exit()  # exit the script
    # endif


# enddef


# Preprocess the corpus
def preprocess(corpus):
    # find all the rare words
    freqDict = defaultdict(int)
    for sen in corpus:
        for word in sen:
            freqDict[word] += 1
    # endfor
    # endfor

    # replace rare words with unk
    for sen in corpus:
        for i in range(0, len(sen)):
            word = sen[i]
            print(word)
            print(freqDict[word])
            if freqDict[word] < 2:

                sen[i] = UNK
    # endif
    # endfor
    # endfor

    # bookend the sentences with start and end tokens
    for sen in corpus:
        sen.insert(0, start)
        sen.append(end)
    # endfor

    return corpus


# enddef


def preprocessTest(vocab, corpus):
    # replace test words that were unseen in the training with unk
    for sen in corpus:
        for i in range(0, len(sen)):
            word = sen[i]
            if word not in vocab:
                sen[i] = UNK
    # endif
    # endfor
    # endfor

    # bookend the sentences with start and end tokens
    for sen in corpus:
        sen.insert(0, start)
        sen.append(end)
    # endfor

    return corpus


# enddef

# Constants
UNK = "UNK"  # Unknown word token
start = "<s>"  # Start-of-sentence token
end = "</s>"  # End-of-sentence-token


# --------------------------------------------------------------
# Language models and data structures
# --------------------------------------------------------------


# Parent class for the three language models you need to implement
class LanguageModel:
    # Initialize and train the model (ie, estimate the model's underlying probability
    # distribution from the training corpus)
    def __init__(self, corpus):
        print(
            """Your task is to implement four kinds of n-gram language models:
      a) an (unsmoothed) unigram model (UnigramModel)
      b) a unigram model smoothed using Laplace smoothing (SmoothedUnigramModel)
      c) an unsmoothed bigram model (BigramModel)
      d) a bigram model smoothed using linear interpolation smoothing (SmoothedBigramModelInt)
      """
        )

    # enddef

    # Generate a sentence by drawing words according to the
    # model's probability distribution
    # Note: think about how to set the length of the sentence
    # in a principled way
    def generateSentence(self):
        print("Implement the generateSentence method in each subclass")
        return "mary had a little lamb ."

    # emddef

    # Given a sentence (sen), return the probability of
    # that sentence under the model
    def getSentenceProbability(self, sen):
        print("Implement the getSentenceProbability method in each subclass")
        return 0.0

    # enddef

    # Given a corpus, calculate and return its perplexity
    # (normalized inverse log probability)
    def getCorpusPerplexity(self, corpus):
        print("Implement the getCorpusPerplexity method")
        return 0.0

    # enddef

    # Given a file (filename) and the number of sentences, generate a list
    # of sentences and write each to file along with its model probability.
    # Note: you shouldn't need to change this method
    def generateSentencesToFile(self, numberOfSentences, filename):
        filePointer = open(filename, "w+")
        for i in range(0, numberOfSentences):
            sen = self.generateSentence()
            prob = self.getSentenceProbability(sen)

            stringGenerated = str(prob) + " " + " ".join(sen)
            print(stringGenerated, end="\n", file=filePointer)


# endfor
# enddef
# endclass


# Unigram language model
class UnigramModel(LanguageModel):
    def __init__(self, corpus):
        # print("Subtask: implement the unsmoothed unigram language model")
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
        return self.counts[word] / self.total

    def draw(self):
        rand = random.random()
        for word in self.counts.keys():
            rand -= self.prob(word)
            if rand <= 0.0:
                return word

    def generateSentence(self):
        sent = [start]
        while 1:
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
            logsum += self.getSentenceLogProbability(sen)
        return math.exp(-logsum/self.total)

    # endddef


# endclass


# Smoothed unigram language model (use laplace for smoothing)
class SmoothedUnigramModel(LanguageModel):
    def __init__(self, corpus):
        # print("Subtask: implement the smoothed unigram language model")
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
        while 1:
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
            #logsum += math.log(self.getSentenceProbability(sen)) same as below
            logsum += self.getSentenceLogProbability(sen)
        return math.exp(-logsum/self.total)

    # endddef


# endclass


# Unsmoothed bigram language model
class BigramModel(LanguageModel):
    def __init__(self, corpus):
        # print("Subtask: implement the unsmoothed bigram language model")
        self.double_count = defaultdict(float)
        self.single_count = defaultdict(float)
        self.following = defaultdict(set)

        self.total_pair_num = 0
        self.corpus = corpus
        self.train(corpus)

    def train(self, corpus):
        for sen in corpus:
            for i in range(len(sen)):
                if i != len(sen) - 1:
                    self.double_count[(sen[i], sen[i + 1])] += 1.0
                    self.following[sen[i]].add(sen[i + 1])
                    self.total_pair_num += 1.0
                self.single_count[sen[i]] += 1.0

    def test(self):
        pass

    def prob(self, word, prevword):
        return self.double_count[(prevword, word)] / self.single_count[prevword]

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
        while 1:
            newword = self.draw(lastword)
            sent.append(newword)
            if newword == end:
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
        small_positive_value = 1e-25
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

    # enddef


# endclass


# Smoothed bigram language model (use linear interpolation for smoothing, set lambda1 = lambda2 = 0.5)
class SmoothedBigramModelInt(LanguageModel):
    def __init__(self, corpus):
        self.corpus = corpus
        self.unigram_counts = defaultdict(float)
        self.bigram_counts = defaultdict(float)
        self.train(corpus)

    def train(self, corpus):
        for sentence in corpus:
            for i in range(len(sentence) - 1):
                self.unigram_counts[sentence[i]] += 1.0
                self.bigram_counts[(sentence[i], sentence[i + 1])] += 1.0
            self.unigram_counts[sentence[-1]] += 1.0

    def prob(self, word, prevword, lambda1=0.5, lambda2=0.5):
        unigram_prob = self.unigram_counts[word] / sum(self.unigram_counts.values())
        bigram_prob = (
            self.bigram_counts[(prevword, word)] / self.unigram_counts[prevword]
            if self.unigram_counts[prevword] > 0
            else 0
        )
        return lambda1 * bigram_prob + lambda2 * unigram_prob

    def generateSentence(self):
        sentence = [start]
        while True:
            next_word_candidates = [
                word
                for word in self.unigram_counts.keys()
                if (sentence[-1], word) in self.bigram_counts
            ]
            if not next_word_candidates:
                break
            probabilities = [
                self.prob(word, sentence[-1]) for word in next_word_candidates
            ]
            next_word = random.choices(next_word_candidates, probabilities)[0]
            sentence.append(next_word)
            if next_word == end:
                break
        return sentence


    def getSentenceProbability(self, sentence):
        log_probability = 0.0
        for i in range(len(sentence) - 1):
            prob = self.prob(sentence[i + 1], sentence[i])
            if prob > 0:
                log_probability += np.log(prob)
        return log_probability

    def getCorpusPerplexity(self, corpus):
        total_log_prob = 0
        total_word_count = 0
        for sentence in corpus:
            total_log_prob += self.getSentenceProbability(sentence)
            total_word_count += len(sentence)
        return np.exp(-total_log_prob / total_word_count)

    # enddef


# endclass


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

    # endddef

    # Add observed counts from corpus to the distribution
    def train(self, corpus):
        for sen in corpus:
            for word in sen:
                if word == start:
                    continue
                self.counts[word] += 1.0
                self.total += 1.0
            # endfor
        # endfor

    # enddef

    # Returns the probability of word in the distribution
    def prob(self, word):
        return self.counts[word] / self.total

    # enddef

    # Generate a single random word according to the distribution
    def draw(self):
        rand = random.random()
        for word in self.counts.keys():
            rand -= self.prob(word)
            if rand <= 0.0:
                return word

    # endif


# endfor
# enddef
# endclass

# -------------------------------------------
# The main routine
# -------------------------------------------
if __name__ == "__main__":

    # following portion was originally in the end, repurposed to use pickle resume functionality
    pkls = ["trainCorpus.pkl", "posTestCorpus.pkl", "negTestCorpus.pkl"]
    # if files exist from pkls list
    if all(os.path.isfile(pkl) for pkl in pkls):
        trainCorpus = pickle.load(open(pkls[0], "rb"))
        posTestCorpus = pickle.load(open(pkls[1], "rb"))
        negTestCorpus = pickle.load(open(pkls[2], "rb"))
        # jump to last portion of code
        # Run sample unigram dist code
        unigramDist = UnigramDist(trainCorpus)
        print("Sample UnigramDist output:")
        print('Probability of "picture": ', unigramDist.prob("picture"))
        print('"Random" draw: ', unigramDist.draw())

        unigramDist = UnigramDist(trainCorpus)
        unigramModel = UnigramModel(trainCorpus)
        smoothedUnigramModel = SmoothedUnigramModel(trainCorpus)
        bigramModel = BigramModel(trainCorpus)
        smoothedBigramModelInt = SmoothedBigramModelInt(trainCorpus)
        
        print("3:additional sentences using your bigram and smoothed bigram models")
        
        for i in range(3):
            print("Bgram model output:")
            print(bigramModel.generateSentence())
            print("smooted bgram output:")
            print(smoothedBigramModelInt.generateSentence())
        
        
        unigramModel.generateSentencesToFile(numberOfSentences=20, filename='unigram_output.txt')
        smoothedUnigramModel.generateSentencesToFile(numberOfSentences=20, filename='smooth_unigram_output.txt')
        bigramModel.generateSentencesToFile(numberOfSentences=20, filename='bigram_output.txt')
        smoothedBigramModelInt.generateSentencesToFile(numberOfSentences=20, filename='smooth_bigram_int_output.txt')
        
        print("The preplexity of the positive test corpus of the unigram model is", unigramModel.getCorpusPerplexity(posTestCorpus))
        print("The preplexity of the negitive test corpus of the unigram model is", unigramModel.getCorpusPerplexity(negTestCorpus))

        print("The preplexity of the positive test corpus of the smoothed unigram model is", smoothedUnigramModel.getCorpusPerplexity(posTestCorpus))
        print("The preplexity of the negative test corpus of the smoothed unigram model is", smoothedUnigramModel.getCorpusPerplexity(negTestCorpus))
        
        print('The preplexity of the positive test corpus of the biagram model is', bigramModel.getCorpusPerplexity(posTestCorpus))
        print('The preplexity of the negaive test corpus of the biagram model is', bigramModel.getCorpusPerplexity(negTestCorpus))
        
        print("The preplexity of the positive test corpus of the smoothed biagram model with linear interpolation is", smoothedBigramModelInt.getCorpusPerplexity(posTestCorpus))
        print("The preplexity of the negative test corpus of the smoothed biagram model with linear interpolation is", smoothedBigramModelInt.getCorpusPerplexity(negTestCorpus))

        print('Finished')
        sys.exit()

    # read your corpora
    trainCorpus = readFileToCorpus("train.txt")
    trainCorpus = preprocess(trainCorpus)

    posTestCorpus = readFileToCorpus("pos_test.txt")
    negTestCorpus = readFileToCorpus("neg_test.txt")

    vocab = set()
    # Please write the code to create the vocab over here before the function preprocessTest
    # print("""Task 0: create a vocabulary(collection of word types) for the train corpus""")
    for sen in trainCorpus:
        for word in sen:
            vocab.add(word)

    posTestCorpus = preprocessTest(vocab, posTestCorpus)
    negTestCorpus = preprocessTest(vocab, negTestCorpus)

    # save to pickle (resume code)
    pickle.dump(trainCorpus, open(pkls[0], "wb"))
    pickle.dump(posTestCorpus, open(pkls[1], "wb"))
    pickle.dump(negTestCorpus, open(pkls[2], "wb"))
    print("Pickles are generated... rerun the code to get sample outputs")
    sys.exit()

#     Questions
# 1. When generating sentences with the unigram model, what controls the length of the generated
# sentences? How does this differ from the sentences produced by the bigram models?

# >Unigram Model: The length of the sentences generated by the unigram model is not controlled by the model itself. 
# It’s usually set by a predefined length or until a stop token (like </s>) is generated. The unigram model generates each word independently,
# based on the probability of each word in the corpus. 
# 
# Bigram Model: The bigram model, on the other hand, generates sentences based on the probability of a word given the previous word. 
# This makes the sentence length more dependent on the actual language structure and can result in more realistic sentence lengths.

# 2. Consider the probability of the generated sentences according to your models. Do your models assign
# drastically different probabilities to the different sets of sentences? Why do you think that is?

# Yes, the models can assign drastically different probabilities to the different sets of sentences. 
# This is because each model has a different way of calculating the probability of a sentence. The unigram model only considers the
# individual probability of each word, while the bigram model considers the probability of a word given the previous word. 
# Therefore, a sentence that seems likely under a unigram model might seem unlikely under a bigram model, and vice versa. 
# The probabilities provided in the bigram_output.txt and smoothed_bigram_int_output.txt files are a clear example of this. 
# The probabilities assigned by the bigram model are much higher than those assigned by the smoothed bigram model. 
# This is because the smoothed bigram model uses interpolation or backoff to handle unseen bigrams, which results in lower probabilities 
# for sentences overall. 
# On the other hand, the bigram model assigns zero probability to unseen bigrams, so its probabilities are only based on seen bigrams 
# in the training data, which can result in higher probabilities for sentences. However, this also means that the bigram model is less robust
# to unseen data compared to the smoothed bigram model.

# 3. Generate additional sentences using your bigram and smoothed bigram models. In your opinion,
# which model produces better / more realistic sentences?

# >The generated sentences from my bigram and smoothed bigram models are as follows:
# 
# Bigram model output: '<s>', 'i', 'hate', 'about', 'mortality', 'rate', '.', '</s>'
# Smoothed bigram output: '<s>', 'the', 'stellar', ',', 'where', 'she', 'suggests', 'that', 'working', 'in', '.', '</s>'
# In my opinion, the smoothed bigram model generally produces more realistic sentences. 
# This is because it takes into account not only the frequency of word pairs (like the bigram model) but also the individual frequencies
# of words (like the unigram model), which can result in a better balance between respecting the data and generalizing to new inputs.


# 4. For each of the four models, which test corpus has a higher perplexity? Why? Make sure to include
# the perplexity values in the answer.

# >The perplexity values for each model are: 
# 
# Unigram model: Positive test corpus - 1.2459, Negative test corpus - 1.2335
# Smoothed unigram model: Positive test corpus - 1.2461, Negative test corpus - 1.2337
# Bigram model: Positive test corpus - 1.7234, Negative test corpus - 1.7011
# Smoothed bigram model: Positive test corpus - 200.9670, Negative test corpus - 205.3751
# For each of the four models, the positive test corpus has a higher perplexity. 
# This could be due to various reasons such as the positive corpus being more diverse or complex than the negative corpus,
# leading to a higher perplexity value. Perplexity is how well a probability model predicts a sample and a lower perplexity score 
# indicates better generalization performance.
