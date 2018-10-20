from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import codecs
import util
import dataImporter
tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = util.getStopWords('stopwords.txt')
    
userinput = str(raw_input('Enter your list: '))    
channel_list = []
for input in userinput.split(','):
        channel_list.append(input)
for channel in channel_list:
        dataImporter.writeChannelMessagesToFile(channel+'.txt', channel)

doc_set = []
for channel in channel_list:
    doc = 'doc_' + channel
    doc = codecs.open(channel+'.txt', encoding='utf-8').read()
    doc_set.append(doc)


# list for tokenized documents in loop
texts = []

# loop through document list
for doc in doc_set:
    
# clean and tokenize document string
    raw = doc.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]

    # # add tokens to list
    texts.append(stopped_tokens)


# # turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# # # convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

n_topics = int(raw_input("Enter the number of topics: "))
n_passes = int(raw_input("Enter the number of passes: "))

# # # generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=n_topics, id2word = dictionary, passes=n_passes)

output = ldamodel.print_topics(num_topics=2, num_words=20)
print("Topic 0 ---> ", output[0])
print("\n")
print("Topic 1 ---> ", output[1])
