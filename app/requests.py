from app import app
import urllib.request,json
from .models import news

News = news.News
Source = news.Source

#create an  API request
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["ARTICLES_API_BASE_URL"]
source_url = app.config['NEWS_SOURCES_BASE_URL']

def get_news(everything):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(everything,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
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
        id = news_article.get("source id")
        source = news_article.get('source name')
        title = news_article.get('title')
        description = news_article.get('description')
        url = news_article.get('url')
        urlToImage = news_article.get('urlToImage')
        publishedAt = news_article.get('publishedAt')

        if urlToImage:
            news_object = News(id,source,title,description,url,urlToImage,publishedAt)
            news_results.append(news_object)

    return news_results

def get_sources():
    '''
    Function that gets the json response to our url request
    '''Usage history

    get_sources_url = source_url.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
    return sources_results
def process_sources(sources_list):
    '''
    Function that processes the news sources results and turns them into a list of objects
    Args:
        sources_list: A list of dictionaries that contain sources details
    Returns:
        sources_results: A list of sources objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        language = source_item.get('language')
        country = source_item.get('country')
        sources_object = Source(id,name,description,url,country,language)
        sources_results.append(sources_object)
    return sources_results


def get_article(id):
    get_article_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_object = None
        if article_details_response:
            id = article_details_response.get('source id')
            source =  article_details_response.get('source.name')
            title1 =  article_details_response.get('title')
            description =  article_details_response.get('description')
            url =  article_details_response.get('url')
            urlToImage =  article_details_response.get('urlToImage')
            publishedAt =  article_details_response.get('publishedAt')
            article_object = News(id,source,title,description,url,urlToImage,publishedAt)
    return article_object

def search_news(news_name):
    search_news_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)


    return search_news_results