import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = simi_matrix[movie_index]
    movie_list = sorted(list(enumerate(simi_matrix[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_name =[]
    recommended_movie_poster =[]
    for i in movie_list:
        # Fetching Movie Poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_name.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movies_name,recommended_movie_poster


movie_matrix = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movie_matrix)

simi_matrix =  pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

movie_list = movies['title'].values
selected_movie_name = st.selectbox(
    'How would like to be contacted?',
    movie_list)

if st.button('Recommend'):
    recommendation_movie_name,recommendation_movie_poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendation_movie_name[0])
        st.image(recommendation_movie_poster[0])
    with col2:
        st.text(recommendation_movie_name[1])
        st.image(recommendation_movie_poster[1])

    with col3:
        st.text(recommendation_movie_name[2])
        st.image(recommendation_movie_poster[2])
    with col4:
        st.text(recommendation_movie_name[3])
        st.image(recommendation_movie_poster[3])
    with col5:
        st.text(recommendation_movie_name[4])
        st.image(recommendation_movie_poster[4])




