# importing required libraries
import numpy as np
import pandas as pd
import ast
import nltk
# nltk.download('all')
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests

def convert(text):
    L =[]
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

def convert3(text):
    L =[]
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
        counter+=1
    return L

def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L


def stem(text,ps):
   
    y = []
    for i in text.split():
        y.append(ps.stem(i))
        
    return " ".join(y)

def init():
    #importing dataset
    movies = pd.read_csv('./data/movie_recommendation_system_dataset/tmdb_5000_movies.csv')
    credits = pd.read_csv('./data/movie_recommendation_system_dataset/tmdb_5000_credits.csv') 

    # merging the datasets
    movies = movies.merge(credits, on='title')
    movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]
    movies.dropna(inplace=True)

    movies['genres'] = movies['genres'].apply(convert)

    movies['keywords'] = movies['keywords'].apply(convert)

    movies['cast'] = movies['cast'].apply(convert3)

    movies['crew'] = movies['crew'].apply(fetch_director)

    movies['overview'] = movies['overview'].apply(lambda x:x.split())

    movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ", "") for i in x])
    movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ", "") for i in x])
    movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ", "") for i in x])
    movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ", "") for i in x])

    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

    movies_df = movies[['movie_id', 'title', 'tags']]

    movies_df['tags'] = movies_df['tags'].apply(lambda x:" ".join(x))

    movies_df['tags'] = movies_df['tags'].apply(lambda x:x.lower())
    
    ps = PorterStemmer()
    movies_df['tags'] = movies_df['tags'].apply(lambda x: stem(x,ps))
    
    return movies_df

def calc_cos_sim(dframe):
    
    cv = CountVectorizer(max_features=5000, stop_words='english')

    vectors = cv.fit_transform(dframe['tags']).toarray()

    similarity = cosine_similarity(vectors)

    return similarity
    
def recommend(movie,dframe,sim):
    index = dframe[dframe['title'] == movie].index[0]
    distances = sim[index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommend_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommend_movies.append(str(dframe.iloc[i[0]].title))  
    return recommend_movies

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=a90a90d766be503859ba6525546ae6ea&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

    recommend_movies_posters = []
    recommend_movies_posters.append(fetch_poster(movie_id))
    recommend_movies_posters