# importing required libraries
import numpy as np
import pandas as pd
import ast
import nltk
# nltk.download('all')
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


#importing dataset
movies = pd.read_csv('../data/movie_recommendation_system_dataset/tmdb_5000_movies.csv')
credits = pd.read_csv('../data/movie_recommendation_system_dataset/tmdb_5000_credits.csv') 

# merging the datasets
movies = movies.merge(credits, on='title')
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]
movies.dropna(inplace=True)


def convert(text):
    L =[]
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)

movies['keywords'] = movies['keywords'].apply(convert)

def convert3(text):
    L =[]
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
        counter+=1
    return L

movies['cast'] = movies['cast'].apply(convert3)

def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L 

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

def stem(text):
    y = []
    
    for i in text.split():
        y.append(ps.stem(i))
        
    return " ".join(y)

movies_df['tags'] = movies_df['tags'].apply(stem)

cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(movies_df['tags']).toarray()

similarity = cosine_similarity(vectors)

def recommend(movie):
    index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    
    for i in movies_list:
        print(movies_df.iloc[i[0]].title)
recommend('Pirates of the Caribbean: At World\'s End')