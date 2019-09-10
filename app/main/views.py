
from . import main
from ..requests import get_news,get_article,search_news,get_sources
from flask import render_template,request,redirect,url_for

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Welcome to Epica News Highlights"
    message = 'Welcome to Epica News'

    # Getting news categories
    entertainment_highlights = get_news('entertainment')
    business_news = get_news('business')
    tech_news = get_news('technology')
    sports_news = get_news('sports')
    health_news = get_news('health')
    life_style =get_news('lifestyle')
    breaking_news = get_news('breaking')
    news_sources = get_sources()

    # print(news_highlights)

   
    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_name = search_news))
    else:


        return render_template('index.html',text=message, title = title, entertainment = entertainment_highlights,
    business = business_news,technology =tech_news,sports = sports_news,health = health_news,
    lifestyle = life_style,breaking=breaking_news,sources=news_sources)




@main.route('/article/id')
def article(id):

    '''
    View article page function that returns the article details page and its data
    '''
    article = get_article(id)
    title = f'{article.title}'

    return render_template('article.html',title = title,article = article)


@main.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list =news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'

    return render_template('search.html',news = searched_news)