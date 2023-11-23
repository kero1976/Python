from aws.s3 import check, get

from logging import getLogger

logger = getLogger(__name__)


def get_list(bucket_name, prefix=""):
    logger.debug(
        {
            "action": "start",
            "param": {"bucket_name": bucket_name, "prefix": prefix},
        }
    )
    try:
        s3 = get.get_client()
        response = get.get_filepath_list(s3, bucket_name, prefix)
        if check.response_code(response) == 200:
            contents = check.response_get_contents(response)
            result = check.contents_parse(contents)
            return result
    except Exception as e:
        logger.error(
            {
                "action": "fail",
                "param": {"s3": s3, "bucket_name": bucket_name, "prefix": prefix},
                "exception": e,
            }
        )
