from dotenv import load_dotenv
from loguru import logger

from media_retrieval.utils import constants  # noqa: F401

# Load environment variables from .env file if it exists
load_dotenv()


# If tqdm is installed, configure loguru with tqdm.write
# https://github.com/Delgan/loguru/issues/135
try:
    from tqdm import tqdm

    logger.remove(0)
    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass
