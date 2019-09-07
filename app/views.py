from flask import render_template
from app import app
from .requests import get_news


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Welcome to Epica News Highlights"
    message = 'Welcome to Epica News'

    # Getting popular movie
    news_highlights = get_news('entertainment')
    print(news_highlights)
   


    return render_template('index.html',text=message, title = title, entertainment = news_highlights)