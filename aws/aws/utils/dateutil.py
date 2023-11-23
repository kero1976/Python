from logging import getLogger
from datetime import datetime

logger = getLogger(__name__)


def to_str(date: datetime) -> str:
    """datetimeを日本時刻のYYYY/MM/DD HH24:MI:SS形式にする

    Args:
        date (datetime): _description_

    Returns:
        str: _description_
    """
    logger.debug({"action": "start", "param": {"date": date}})
    response = date.strftime("%Y/%m/%d %H:%M:%S")
    logger.info({"action": "success", "response": response})
    return response
