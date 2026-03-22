import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_movie_from_omdb(title):
    url = f"https://www.omdbapi.com/?t={title}&apikey={os.getenv('OMDB_API_KEY')}"
    response = requests.get(url)
    data = response.json()

    if data['Response'] == 'False':
        return None
    
    return data

def search_movies_from_omdb(title): 
    url = f"https://www.omdbapi.com/?s={title}&apikey={os.getenv('OMDB_API_KEY')}"
    response = requests.get(url)
    data = response.json()

    if data['Response'] == 'False':
        return None
    
    return data

def get_movie_from_id(id):
    url = f"https://www.omdbapi.com/?i={id}&apikey={os.getenv('OMDB_API_KEY')}"
    response = requests.get(url)
    data = response.json()

    if data['Response'] == 'False':
        return None
    
    return data