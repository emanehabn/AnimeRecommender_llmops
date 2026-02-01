from lark import logger
from src import vector_store
from src.vector_store import VectoreStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exceptions import CustomException

logger = get_logger(__name__)


class AnimeRecommendationPipeline:
    def __init__(self, persist_dir="chroma_db"):
        try:
            logger.info ("Initializing Recommendation pipeline")
            
            # create new vector store
            vector_build = VectoreStoreBuilder(csv_path="", persist_dir=persist_dir)

            retriever = vector_build.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever, GROQ_API_KEY, MODEL_NAME)

            logger.info("Pipeline Intailizes Successfully")
            
        except Exception as e:
            logger.error(f"Failed to intialize recommendation pipeline {str(e)}")

            raise CustomException("Error during pipeline intialization")

    def recommend(self, query:str) -> str:
        try:
            logger.info(f"Recieved a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated successfully")

            return recommendation
        
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")

            raise CustomException("Error while recommendation generation")

