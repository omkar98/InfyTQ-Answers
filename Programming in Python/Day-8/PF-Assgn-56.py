
#PF-Assgn-56

import collections

from collections import Counter

def max_frequency_word_counter(data):
    data = data.lower()
    words = data.split()
    words = Counter(words)
    
    total = words.most_common()
    total = dict(words.most_common())
    
    total = (sorted(total.items(), key=lambda kv: kv[1], reverse = True))
    
    max_freq = 0
    
    for i in range(1,len(total)-1):
            if total[0][1] == (total[i][1]):
                if len(total[max_freq][0]) < len(total[i][0]):
                    max_freq = i
    
    word = total[max_freq][0]
    frequency = total[max_freq][1]
    
    if frequency == 1:
        return None
    else:
        print(word,frequency)
        
    #print(word)

#Provide different values for data and test your program.
data="Courage is not the absence of fear but rather the judgement that something else is more important than fear"
max_frequency_word_counter(data)
