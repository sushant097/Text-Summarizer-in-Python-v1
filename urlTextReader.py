import urllib.request
from bs4 import BeautifulSoup
from new_summarizer_text import FrequencySummarizer as fs

def get_only_text(url):
     """
     return the title and the text of the article
     at the specified url
     """
     req = urllib.request.Request(url)
     page = urllib.request.urlopen(req).read().decode('utf8')
     soup = BeautifulSoup(page,"html5lib")
     text =' '.join(map(lambda p: p.text,soup.find_all('p')))
     return soup.title.text,text

# We cab finally apply our summarizer on a set of articles extracted from the BBC news feed
while True:
     url = input("Please enter the url to read the text, make sure enter the full URL:\n")
     if(url != ""):
          
          req = urllib.request.Request(url)
          try:feed_xml = urllib.request.urlopen(url).read()
          except urllib.error.URLError as e:
               print(e.reason)
          feed = BeautifulSoup(feed_xml.decode('utf-8'),"html5lib")
          to_summarize = list(map(lambda p: p.text, feed.find_all('guid')))
          #fs = FrequencySummarizer()
          
          #fs = FrequencySummarizer()
          
          for article_url in to_summarize[:5]:
               title,text = get_only_text(article_url)
               print("------------------------------------------------")
               print(title)
               for s in fs.summarize(text, 2):
                    print('*',s)
          break;

     else:
          print("ENter the url to summarize the text\n")

