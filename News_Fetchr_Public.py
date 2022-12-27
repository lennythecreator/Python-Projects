import requests
from sys import argv

url = 'https://newsapi.org/v2/top-headlines?'
API_KEY = "" #Add your Api key here

def Get_Article_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy" : "top",
        "country" : "us",
        "apiKey" : API_KEY
    }
    return _get_articles(query_parameters)

def Get_Article_by_query(query):
    query_parameters={
        "q": query,
        "sortBy" : "top",
        "country" : "us",
        "apiKey" : API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(url,params=params)

    articles= response.json()['articles']

    results = []

    for article in articles:
        results.append({"title":article["title"],"url":article["url"]})
    
    for result in results:
        print(result['title'])
        print(result['url'])
        print('')

def get_Sources_by_Category(category):
    pass

if __name__ == "__main__":
    User_input=input("Enter the category of news you would like: ")
    print(f"Getting news for {User_input}...\n")
    Get_Article_by_category(User_input)
    print(f"Successfuly get top {User_input} headlines!")