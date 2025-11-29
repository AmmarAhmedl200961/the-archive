import re
# Removes space form a urdu word 
def remove(string):
    return string.replace(" ", "")
    
def stem(word: str):
    """ Stem a word using a simple rule-based algorithm."""
    allUrduAffixes = {}
    wrongGuessedStem = {}
    totalWords = 0
    totalCorrectGuessed = 0
    

    urduPrefixes = ['بے', 'بد', 'لا', 'ہے', 'نا', 'با', 'کم', 'ان', 'اہل', 'کم']
    urduSuffixes = ['دار', 'وں', 'یاں', 'یں', 'ات', 'گوار', 'ور', 'پسند']

    

    # Opening the file which contains all urdu words and their respective stems
    urduFile = open("urdu-affixes.txt", "r", encoding="utf-8")
    for urduWord in urduFile:
        totalWords = totalWords + 1
        x = urduWord.splitlines()
        x = x[0].split('\t\t')
        # Adding real word and its real stem in allUrduAffixes dictionary
        allUrduAffixes[x[0]] = x[1]
    # Stemming the input word
    urduWord = word
    prefixFound = False
    foundBothPrefixSuffix = False
    
    predictedStem = urduWord

    if not foundBothPrefixSuffix:
        for prefix in urduPrefixes:
            checkPrefix = re.search(rf'\A{prefix}', urduWord)
            if checkPrefix:
                predictedStem = urduWord[checkPrefix.span(0)[1]:]
                prefixFound = True
                realStem = remove(allUrduAffixes[word])
                predictedStem = remove(predictedStem)
                if predictedStem == realStem:
                    totalCorrectGuessed = totalCorrectGuessed + 1
                else:
                    temp = {
                        "realStem": realStem,
                        "predictedStem": predictedStem,
                    }
                    wrongGuessedStem[urduWord] = temp
                break

    if not prefixFound:
        for suffix in urduSuffixes:
            checkSuffix = re.search(rf"{suffix}\Z", urduWord)
            if checkSuffix:
                predictedStem = urduWord[:checkSuffix.span(0)[0]]
                realStem = remove(allUrduAffixes[word])
                predictedStem = remove(predictedStem)
                if predictedStem == realStem:
                    totalCorrectGuessed = totalCorrectGuessed + 1
                else:
                    temp = {
                        "realStem": realStem,
                        "predictedStem": predictedStem,
                    }
                    wrongGuessedStem[urduWord] = temp
                break
    return remove(predictedStem)
