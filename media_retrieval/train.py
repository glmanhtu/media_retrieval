import hydra
from omegaconf import DictConfig

from media_retrieval.utils.constants import CONFIG_DIR


@hydra.main(config_path=str(CONFIG_DIR), config_name="main", version_base=None)
def main(config: DictConfig):
    print("hello")


if __name__ == "__main__":
    main()
