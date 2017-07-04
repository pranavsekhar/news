import newspaper
from parse_utils import *

class User():
	def __init__(self, name, topics):
		self.name = name
		self.topics = topics

url_dictionary = {} # populate with selected topics

def driver(user):
	topics = user.topics
	article_dictionary = get_article_dictionary(topics)

def get_article_dictionary(topics):
	article_dictionary = {}
	for i in range(len(topics)):
		query_url = url_dictionary[topics[i]]
		google_build = newspaper.build(query_url, memoize_articles = False)
		article_list = []
		for article in google_build.articles:
			article_list.append(article)
		article_list = article_list[1:21]
		
		for article in article_list:
			curr_article = article
			curr_article.download()
			curr_article.parse()
			curr_article.nlp()
			print(curr_article.summary)