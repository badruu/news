import urllib.request,json
from .models import Source,Article

# Article=article.Article
# Source = source.Source


api_key = 'd2b77818e9674bfd91dc2114b7540de0'
# base_url = None
# article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    article_url=app.config['ARTICLE_API_BASE_URL']

def get_source(category):
    '''
    function that gets json response to our url request
    '''
    get_source_url='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data=url.read()
        get_source_response=json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    function that pricesses the source results and makes them into a list of objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns :
        source_results: A list of source objects
    '''

    source_results=[]
    for source in source_list:
        id=source.get('id')
        name=source.get('name')
        description=source.get('description')
        url=source.get('url')
        category=source.get('category')
        language=source.get('language')
        country=source.get('country')

        if id:
            source_Object = Source(id,name,description,url,category,language,country)
            source_results.append(source_Object)

    return source_results

def get_article(id):
    '''
    function that gets json response to the url request
    '''
    get_article_url='https://newsapi.org/v2/everything?q={}&apiKey={}'.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data=url.read()
        get_article_response=json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = receive_result(article_results_list)

    return article_results

def receive_result(article_list):
    '''
    function processing article result and making them into list of objects

    Args:
        article_list: a list of dictionaries that contain article details

    returns:
        article_results: a list of article objects

    '''

    article_results=[]
    for article in article_list:
        id=article.get('id')
        name = article.get('name')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')

        if author:
            article_object = Article(id,name,author,title,description,url,urlToImage,publishedAt,content)
            article_results.append(article_object)

    return article_results