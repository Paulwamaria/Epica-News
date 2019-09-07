from app import app
import urllib.requests,json
from .models import news

News = news.News

#create an  API request
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["ARTICLES_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results


def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of articles objects
    '''
    news_results = []
    for news_article in news_list:
        source = news_article.get('source.name')
        title = news_article.get('title')
        description = news_article.get('description')
        url = news_article.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_article.get('publishedAt')

        if urlToImage:
            news_object = News(source,title,description,url,urlToImage,publishedAt)
            news_results.append(news_object)

    return news_results