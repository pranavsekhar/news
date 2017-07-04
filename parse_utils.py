def generate_url(topic_name):
	url = '';
	if len(topic_name.split(' ')) == 1:
		url = 'https://news.google.com/news/search/section/q/' + topic_name + '/' + topic_name + '?hl=en&ned=us'
	else: #only handles 2 words for now
		sub_str = ''
		words = topic_name.split(' ')
		for i in range(len(words)):
			if i != len(words) - 1:
				sub_str = sub_str + words[i] + '%20'
			else:
				sub_str = sub_str + words[i]
		url = 'https://news.google.com/news/search/section/q/' + sub_str + '/' + sub_str + '?hl=en&ned=us'
	return url