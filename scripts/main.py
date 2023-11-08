from _common import *

log = logging.getLogger(__name__)

# imports


@hydra.main(str(CONFIG_DIR), "main", None)
def main(cfg: DictConfig):
    """
    This function is the main entry point.

    Args:
        cfg: A configuration object containing the parameters.
    """
    print(cfg)


if __name__ == "__main__":
    main()
