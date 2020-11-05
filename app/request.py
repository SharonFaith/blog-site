import urllib.request,json
from .models import Quote


#Getting quote base url
#base_url = app.config['MOVIE_API_BASE_URL']
base_url = None

def configure_request(app):
    global base_url
    
    base_url = app.config['QUOTES_API_BASE_URL']

def process_results(get_quotes_response):
    
    obj_ect = get_quotes_response
    author = obj_ect.get('author')
    quote = obj_ect.get('quote')

    quote_object = Quote(author, quote)


    return quote_object


def get_quotes():
    '''
    Function that gets the json response to the url request
    '''
    get_quotes_url = base_url

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        
        quotes_results = process_results(get_quotes_response)

    return quotes_results

    print(quotes_results)