import boto3
from logging import getLogger

logger = getLogger(__name__)


def get_filepath_list(s3, bucket_name, prefix="") -> dict:
    """指定したバケットのフォルダ以下のファイルリストを取得する

    Args:
        s3 (_type_): _description_
        bucket_name (_type_): _description_
        prefix (str, optional): _description_. Defaults to "".
    """
    logger.debug(
        {
            "action": "start",
            "param": {"s3": s3, "bucket_name": bucket_name, "prefix": prefix},
        }
    )
    try:
        result = s3.list_objects_v2(Bucket=bucket_name)
        logger.debug(f"type:{type(result)}")
        logger.debug(
            {
                "action": "success",
                "param": {"s3": s3, "bucket_name": bucket_name, "prefix": prefix},
                "result": result,
            }
        )
        print(result)
        return result
    except Exception as e:
        logger.error({"action": "fail", "except": e})
        raise


def get_client():
    logger.debug({"action": "start"})
    result = boto3.client("s3")
    logger.info({"action": "success", "result": result})
    return result
