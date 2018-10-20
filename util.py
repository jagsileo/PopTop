from nltk.corpus import stopwords
import codecs
stopwordsfile = 'stopwords.txt'
def getStopWords(filename) :
    # Stopwords
    try:
        engStopwords = set(line.strip() for line in open(filename))
    except:
        print("Invalid file")   
    engStopwords = engStopwords.union(set(['mr','mrs','one','two','said']))
    nltkStopwords = set(stopwords.words('english'))
    
    return engStopwords.union(nltkStopwords)


def cleanMessages(filename):
    try:
        file = codecs.open(filename, encoding='utf-8')
    except:
        print("Invalid file name")

    words = file.read() 
    filteredWords = []

    # Instantiate a dictionary, and for every word in the file, 
    # Add to the dictionary if it doesn't exist. If it does, increase the count.
    
    # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
    for word in words.lower().split():
       
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("*","")   
        if word not in getStopWords(stopwordsfile): 
            filteredWords.append(word)
        
    file.close()
    return filteredWords        