from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source,get_article

@main.route('/')
def index():
    '''
    root page returning index page
    '''
    General_category=get_source("general")
    Business_category=get_source("business")
    Entertainment_category=get_source("entertainment")
    Health_category=get_source("health")
    Science_category=get_source("science")
    Technology_category=get_source('technology')
    Sports_category=get_source('sports')


    title='News Highlight'
    return render_template('index.html',title=title,general=General_category,business=Business_category,entertainment=Entertainment_category,health=Health_category,science=Science_category,technology=Technology_category,sports=Sports_category)
    

@main.route('/article/<id>')
def article(id):
    '''
    article that return the article details page
    '''

    article=get_article(id)
    print(article)
    title = 'HEADLINES'

    return render_template('article.html',title=title,article=article)