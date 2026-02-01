import os
from urllib import response
from sklearn import pipeline
import streamlit as st
from yarl import Query

from pipeline.pipeline import AnimeRecommendationPipeline

from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exceptions import CustomException


load_dotenv()

st.set_page_config(page_title="Animating4U", layout="wide")


@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("I'm here so you can find your anime mate ❤️\n\n ")

query = st.text_input("Describe your anime preferences: ")

if query:
    with st.spinner("Fetching the animie for you"):
        response = pipeline.recommend(query)
        st.markdown("### I recommend: ")
        st.write(response)

