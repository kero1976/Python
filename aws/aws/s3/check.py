from logging import getLogger

logger = getLogger(__name__)


def response_code(response: dict) -> int:
    """AWSからのレスポンスデータを解析し、HTTPステータスコードを返す

    Args:
        response (dict): Response Data

    Returns:
        int: HTTPStatusCode
    """
    logger.debug({"action": "start", "param": {"response": response}})
    if type(response) is not dict:
        logger.info(
            {"action": "fail", "response": None, "message": "response is None."}
        )
        return None
    metadata = response.get("ResponseMetadata")
    if metadata is None:
        logger.info(
            {"action": "fail", "response": None, "message": "metadata is None."}
        )
        return None
    if type(metadata) is dict:
        code = metadata.get("HTTPStatusCode")
        logger.info({"action": "success", "response": code})
        return int(code)
    else:
        logger.info(
            {
                "action": "fail",
                "response": None,
                "message": f"metadata is {type(metadata)}.",
            }
        )
        return None


def response_get_contents(response: dict) -> list[dict]:
    logger.debug({"action": "start", "param": {"response": response}})
    result = response.get("Contents")
    logger.info({"action": "success", "response": result})
    return result


def contents_parse(contents: list[dict]) -> list[dict]:
    logger.debug({"action": "start", "param": {"contents": contents}})
    # result = []
    # for i in contents:
    #     data = {}
    #     data["Key"] = i["Key"]
    #     data["LastModified"] = i["LastModified"]
    #     result.append(data)

    # result = []
    # for i in contents:
    #     data = {x: y for x, y in i.items() if x in ("Key", "LastModified")}
    #     result.append(data)

    result = [
        {x: y for x, y in i.items() if x in ("Key", "LastModified")} for i in contents
    ]
    logger.info({"action": "success", "response": result})
    print("■" * 100)
    print(result)
    return result
