import datetime
import os
import ast
import time
import collections
from datetime import datetime

import dataImporter
import topicModeler
import util
import wordCounter

def main() :
        """"""""
                # Gets the user input which is a comma separated channel names
                # Fetches the messages using Slack Client API
                # Cleans the messages by removing  stopwords (both NLTK & custom stopwords)
                # Counts the frequency of occurence of the remaining tokens 

        """"""""
        userinput = str(raw_input('Enter your list: '))    
        channel_list = []
        for input in userinput.split(','):
                channel_list.append(input)


        total_count = collections.Counter()
        cleaned_wordlist = {}
        for channel in channel_list:
                dataImporter.writeChannelMessagesToFile(channel+'.txt', channel)
        for channel in channel_list:
                cleaned_words = util.cleanMessages(channel+'.txt')
                cleaned_wordlist[channel] = cleaned_words

        for channel, words in cleaned_wordlist.iteritems():
                 print(channel)
                 total_count.update(wordCounter.countWords(words, channel))

        print("Check out the consolidated output!!")

        
        print("\nThe 10 most common words in all channels are as follows\n")
        
        
        for word, count in total_count.most_common(10):
                print(word, ": ", count)    

if __name__ == "__main__":
        main()