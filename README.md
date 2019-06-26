# Text-Summarizer-in-Python-v1
This program summarize the given paragraph and summarize it. It is of two category such as summarize input text from the keyboard or summarize the text parsed by BeautifulSoup Parser.

The `textSummarizer.py` simply summarize the paragraph given by the keyboard.
The `urlTextReader.py` summarizes the text of the text parsed by the site given as input as in our case bbc news feed.

### Requirements
- NLTK  --> pip install nltk
- Beautiful Soup --> `pip install beautifulsoup4`

#### It is simple to understand. The basic idea is to count the frequency of the words occuring on the text and assume that highest occuring words are important given the threshold of occurence and based upon it, summarize the text.
