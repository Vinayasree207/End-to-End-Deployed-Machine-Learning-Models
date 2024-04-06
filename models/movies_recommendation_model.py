# importing the required libraries
import numpy as np
import pandas as pd
import ast
import nltk
import time
# nltk.download('all')
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests

# converting dict to list and fetching name
def fetch_fields(text):
    L =[]
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

# converting dict to list and fetching nama of first 3 actors/actress
def fetch_3_actors(text):
    L =[]
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
        counter+=1
    return L

# converting dict to list and fetching director name
def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L

# stemming text
def stem(text,ps):
    y = []
    for i in text.split():
        y.append(ps.stem(i))       
    return " ".join(y)

def init():
    # loading the Data
    movies = pd.read_csv('./data/movie_recommendation_system_dataset/tmdb_5000_movies.csv')
    credits = pd.read_csv('./data/movie_recommendation_system_dataset/tmdb_5000_credits.csv') 

    # merging the datasets and creating a copy 
    movies = movies.merge(credits, on='title')
    rawdf = movies.copy()
    movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

    # dropping missing values
    movies.dropna(inplace=True)

    # formatting genre column to list & fetching genres 
    movies['genres'] = movies['genres'].apply(fetch_fields)

    # formatting keyword column to list & fetching keywords 
    movies['keywords'] = movies['keywords'].apply(fetch_fields)

    # formatting column and fetching first 3 actors/actress name
    movies['cast'] = movies['cast'].apply(fetch_3_actors)

    # Formatting columns 'crew' and fetching only the Director of Movie
    movies['crew'] = movies['crew'].apply(fetch_director)

    movies['overview'] = movies['overview'].apply(lambda x:x.split())

    # Removing the white spaces from columns
    movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ", "") for i in x])
    movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ", "") for i in x])
    movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ", "") for i in x])
    movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ", "") for i in x])

    # Creating a new column tags (concat of overview, genres, keywords, cast and crew)
    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

    movies_df = movies[['movie_id', 'title', 'tags']]

    # converting tags list into string
    movies_df['tags'] = movies_df['tags'].apply(lambda x:" ".join(x))

    # lowering the case
    movies_df['tags'] = movies_df['tags'].apply(lambda x:x.lower())
    
    #stemming
    ps = PorterStemmer()
    movies_df['tags'] = movies_df['tags'].apply(lambda x: stem(x,ps))
    
    return movies_df,rawdf

# Calculating Cosine_Similarity matrix of movies in 5000 dimensions 
def calc_cos_sim(dframe):
    
    cv = CountVectorizer(max_features=5000, stop_words='english')

    vectors = cv.fit_transform(dframe['tags']).toarray()

    similarity = cosine_similarity(vectors)

    return similarity

# recommending top 5 similar movies 
def recommend(movie,dframe,sim):
    index = dframe[dframe['title'] == movie].index[0]
    distances = sim[index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommend_movies = []
    for i in movies_list:
        recommend_movies.append(str(dframe.iloc[i[0]].title))  
    return recommend_movies