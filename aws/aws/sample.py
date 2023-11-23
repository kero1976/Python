from logging import getLogger, config
import os
from aws.s3.manager import get_list

config.fileConfig(
    os.path.join(os.path.dirname(__file__), "logging.ini"), encoding="utf-8"
)
logger = getLogger(__name__)


if __name__ == "__main__":
    logger.debug("START")
    result = get_list("u10.jp")
    logger.debug(result)
    print(result)
    logger.debug("END")
