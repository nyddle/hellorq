import requests
from flask_rq import job


@job
def count_words_at_url(url):
    resp = requests.get(url) 
    return len(resp.text.split())

#print count_words_at_url('http://www.yandex.ru')
