from json import load
from src.data_loader import AnimeDataLoader
from src.vector_store import VectoreStoreBuilder
from dotenv import load_dotenv
from config.config import anime_orginal_path, anime_processed_path
from utils.logger import get_logger
from utils.custom_exceptions import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        
        logger.info("Building pipeline is started")

        loader = AnimeDataLoader(anime_orginal_path, anime_processed_path)

        processed_csv = loader.load_and_process()

        logger.info("Data loadeded and processed successufully")

        vector_builder = VectoreStoreBuilder(processed_csv)

        vector_builder.build_save_vectorestore()

        logger.info("Vector store is built successfully.")

        logger.info("Pipeline built successfully")

    except Exception as e:
            logger.error(f"Failed to bulding the vector store {str(e)}")

            raise CustomException("Error during vector store intialization")

         

if __name__ == "__main__":
     main()