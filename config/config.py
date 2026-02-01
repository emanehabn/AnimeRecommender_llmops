import os
from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

MODEL_NAME = "llama-3.1-8b-instant"  #os.getenv("MODEL_NAME")

anime_orginal_path = "/home/eman/Documents/Projects/AnimeRecommender/data/anime_with_synopsis.csv"
anime_processed_path = "/home/eman/Documents/Projects/AnimeRecommender/data/anime_updated.csv"

