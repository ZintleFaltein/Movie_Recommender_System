"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview", "Data analysis and plots"
                    "Meet the team", "Pitch"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[1493:1520])
        movie_2 = st.selectbox('Second Option',title_list[2110:2120])
        movie_3 = st.selectbox('Third Option',title_list[2110:2120])
        # movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        # movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        # movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            top_recommendations = content_model(fav_movies)
            if st.button("Recommend"):
                   st.title("We think you'll like:")
                   for i,j in enumerate(top_recommendations[:10]):
                       st.subheader(str(i+1)+'. '+j)

        if sys == 'Collaborative Based Filtering':
            top_recommendations = collab_model(movie_list=fav_movies,
                                               top_n=10)
            if st.button("Recommend"):
                st.title("We think you'll like:")
                for i,j in enumerate(top_recommendations):
                    st.subheader(str(i+1)+'. '+j)
    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("This is an overview of the models used to recommend movies")

    if page_selection == "Data analysis and plots":
        st.title("Data analysis") 
        st.write("A look at the data analysis")

    if page_selection == "Meet the team":
        st.title("Meet the team")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.



if __name__ == '__main__':
    main()
