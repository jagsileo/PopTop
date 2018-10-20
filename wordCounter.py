import collections, util
#nltk.download()

def countWords(words, channelname):
    wordcount = {}

    for word in words:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    
    
    # Print most common word
    
    n_print = int(input("How many most common words in {} to print? : ".format(channelname)))
    print("\nThe {} most common words in {} are as follows\n".format(n_print, channelname))
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(n_print):
        print(word, ": ", count)        
    return wordcount


    
