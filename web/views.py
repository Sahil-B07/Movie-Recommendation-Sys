from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from django.shortcuts import render
from .models import Movie, Person
import pandas as pd 
import numpy as np 

def landing(request):

    df2=pd.read_csv('/Users/sahilbhor/Work/A-Devops/recommendor/web/tmdb_5000_movies.csv')

    # Create a dictionary to store the top 10 most similar movies
    top_movies = {}
    
    #Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
    tfidf = TfidfVectorizer(stop_words='english')

    #Replace NaN with an empty string
    df2['overview'] = df2['overview'].fillna('')

    #Construct the required TF-IDF matrix by fitting and transforming the data
    tfidf_matrix = tfidf.fit_transform(df2['overview'])
    
    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    #Construct a reverse map of indices and movie titles
    indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()

    # Function that takes in movie title as input and outputs most similar movies
    def get_recommendations(title, cosine_sim=cosine_sim):
        # Get the index of the movie that matches the title
        idx = indices[title]

        # Get the pairwsie similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 5 most similar movies
        sim_scores = sim_scores[1:6]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Store the top 10 most similar movies in the dictionary
        for i, idx in enumerate(movie_indices):
            # top_movies[str(idx)] = df2['title'].iloc[idx]
            if (Movie.objects.filter(title=df2['title'].iloc[idx]).first()):
                top_movies[str(idx)] = Movie.objects.filter(title=df2['title'].iloc[idx]).first()

        # Return the dictionary
        return top_movies
    user = Person.objects.get(first_name='demo')
    for i in user.watched:
        get_recommendations(i)
    
    params = {"movies": top_movies}

    return render(request, "web/index.html", params)