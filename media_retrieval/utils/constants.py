import logging
from pathlib import Path

logger = logging.getLogger(__name__)

PROJ_ROOT = Path(__file__).resolve().parents[2]
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

CONFIG_DIR = PROJ_ROOT / "configs"
