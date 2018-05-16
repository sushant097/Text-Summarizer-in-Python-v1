from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest

class FrequencySummarizer:
     def __init__(self, min_cut=0.1, max_cut=0.9):


          self.min_cut = min_cut
          self.max_cut = max_cut
          self.stopwords = set(stopwords.words("english")+ list(punctuation))
          
     def _compute_frequencies(self, word_sent):
          # compute the frequency of each word

          freq = defaultdict(int)
          for s in word_sent:
               for word in s:
                    if word not in self.stopwords:
                         freq[word] +=1

          # frequencies normalization and filtering
          m = float(max(freq.values()))
          for w in freq.keys():
               freq[w] = freq[w]/m
               if freq[w] >= self.max_cut or freq[w] <= self.min_cut:
                    del freq[w]
               return freq

     def summarize(self, text, n):
          """
           Return a list of n sentences 
           which represent the summary of text.
          """

          sents = sent_tokenize(text)
          assert n <= len(sents)
          word_sent = [word_tokenize(s.lower()) for s in sents]
          self._freq = self._compute_frequencies(word_sent)
          ranking = defaultdict(int)
          for i,sent in enumerate(word_sent):
               for w in sent:
                    if w in self._freq:
                         ranking[i] += self._freq[w]

          sents_idx = self._rank(ranking,n)
          return [sents[j] for j in sents_idx]

     def _rank(self, ranking, n):
              """ return the first n sentences with highest ranking """
              return nlargest(n, ranking, key=ranking.get)
          

"""
text = "" # input text
while True:
     text = input("Enter the text to summarize\n")
     if(len(text)>10):
          break;
     else:
          print("Please input the text as length at least 10")


fs = FrequencySummarizer();

for s in fs.summarize(text,2):
     print("*",s)
     
"""
print("Done!")
