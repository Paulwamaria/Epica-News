from flask import render_template
from app import app
from .requests import get_news,get_article


@app.route('/')
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
    # sports_news = get_news('sports')
    # health_news = get_news('health')
    # life_style =get_news('lifestyle')
    # breaking_news = get_news('breaking')

    # print(news_highlights)
   


    return render_template('index.html',text=message, title = title, entertainment = entertainment_highlights,
    business = business_news,technology =tech_news,sports = sports_news,health = health_news,
    lifestyle = life_style,breaking=breaking_news)

@app.route('/article/id')
def article(id):

    '''
    View article page function that returns the article details page and its data
    '''
    article = get_article(id)
    title = f'{article.title}'

    return render_template('article.html',title = title,article = article)