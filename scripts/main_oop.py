"""
This script defines the main application class and function that initializes and runs the application.
This is written in an object-oriented style.
"""

from _common import *

log = logging.getLogger(__name__)

# imports


class Application:
    """
    A class representing the main application.
    """

    def __init__(self, cfg: DictConfig):
        super().__init__()
        self.cfg = cfg

    def main(self):
        cfg = self.cfg


@hydra.main(
    config_path=str(CONFIG_DIR),
    config_name="main",
    version_base=None,
)
def main(cfg: DictConfig):
    """
    The main function that initializes the application and runs it.

    Args:
        cfg (DictConfig): The configuration dictionary.
    """
    Application(cfg).main()


if __name__ == "__main__":
    main()
