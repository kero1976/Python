from aws.s3 import check
import datetime
from dateutil.tz import tzutc


def test_response_code_200():
    data = {
        "ResponseMetadata": {
            "RequestId": "0Huw1Z3ByG8NbVO5qGb4jOIjHMVEnxJkrQ7izwHrsngqRuqBM3Su",
            "HTTPStatusCode": 200,
            "HTTPHeaders": {
                "x-amzn-requestid": "0Huw1Z3ByG8NbVO5qGb4jOIjHMVEnxJkrQ7izwHrsngqRuqBM3Su"
            },
            "RetryAttempts": 0,
        },
        "IsTruncated": False,
        "Name": "foo",
        "Prefix": "",
        "MaxKeys": 1000,
        "EncodingType": "url",
        "KeyCount": 0,
    }
    result_code = check.response_code(data)
    assert result_code == 200


def test_response_code_none():
    data = None
    result_code = check.response_code(data)
    assert result_code is None


def test_response_code_str():
    data = "aaa"
    result_code = check.response_code(data)
    assert result_code is None


def test_response_code_meta_none():
    data = {}
    result_code = check.response_code(data)
    assert result_code is None


def test_response_code_meta_not_dict():
    data = {"ResponseMetadata": "aaa"}
    result_code = check.response_code(data)
    assert result_code is None


def test_response_get_contents():
    data = {
        "ResponseMetadata": {
            "RequestId": "66w2wcrhhtT1j23qP0iQmkr8HpTiFK1JmfyCM7pJ4D8hIszcgPfy",
            "HTTPStatusCode": 200,
            "HTTPHeaders": {
                "x-amzn-requestid": "66w2wcrhhtT1j23qP0iQmkr8HpTiFK1JmfyCM7pJ4D8hIszcgPfy"
            },
            "RetryAttempts": 0,
        },
        "IsTruncated": False,
        "Contents": [
            {
                "Key": "fuga0.txt",
                "LastModified": datetime.datetime(
                    2023, 11, 19, 0, 22, 20, tzinfo=tzutc()
                ),
                "ETag": '"6ce5f626ed3af11eaae5c0d4c86299a0"',
                "Size": 1028,
                "StorageClass": "STANDARD",
            },
            {
                "Key": "fuga1.txt",
                "LastModified": datetime.datetime(
                    2023, 11, 19, 0, 22, 20, tzinfo=tzutc()
                ),
                "ETag": '"6ce5f626ed3af11eaae5c0d4c86299a0"',
                "Size": 1028,
                "StorageClass": "STANDARD",
            },
            {
                "Key": "fuga2.txt",
                "LastModified": datetime.datetime(
                    2023, 11, 19, 0, 22, 20, tzinfo=tzutc()
                ),
                "ETag": '"6ce5f626ed3af11eaae5c0d4c86299a0"',
                "Size": 1028,
                "StorageClass": "STANDARD",
            },
        ],
        "Name": "foo",
        "Prefix": "",
        "MaxKeys": 1000,
        "EncodingType": "url",
        "KeyCount": 3,
    }
    result_data = check.response_get_contents(data)
    assert result_data == [
        {
            "Key": "fuga0.txt",
            "LastModified": datetime.datetime(2023, 11, 19, 0, 22, 20, tzinfo=tzutc()),
            "ETag": '"6ce5f626ed3af11eaae5c0d4c86299a0"',
            "Size": 1028,
            "StorageClass": "STANDARD",
        },
        {
            "Key": "fuga1.txt",
            "LastModified": datetime.datetime(2023, 11, 19, 0, 22, 20, tzinfo=tzutc()),
            "ETag": '"6ce5f626ed3af11eaae5c0d4c86299a0"',
            "Size": 1028,
            "StorageClass": "STANDARD",
        },
        {
            "Key": "fuga2.txt",
            "LastModified": datetime.datetime(2023, 11, 19, 0, 22, 20, tzinfo=tzutc()),
            "ETag": '"6ce5f626ed3af11eaae5c0d4c86299a0"',
            "Size": 1028,
            "StorageClass": "STANDARD",
        },
    ]


def test_contents_parse():
    data = [
        {
            "Key": "fuga0.txt",
            "LastModified": datetime.datetime(2023, 11, 19, 0, 22, 20, tzinfo=tzutc()),
            "ETag": '"6ce5f626ed3af11eaae5c0d4c86299a0"',
            "Size": 1028,
            "StorageClass": "STANDARD",
        },
        {
            "Key": "fuga1.txt",
            "LastModified": datetime.datetime(2023, 11, 19, 0, 22, 20, tzinfo=tzutc()),
            "ETag": '"6ce5f626ed3af11eaae5c0d4c86299a0"',
            "Size": 1028,
            "StorageClass": "STANDARD",
        },
        {
            "Key": "fuga2.txt",
            "LastModified": datetime.datetime(2023, 11, 19, 0, 22, 20, tzinfo=tzutc()),
            "ETag": '"6ce5f626ed3af11eaae5c0d4c86299a0"',
            "Size": 1028,
            "StorageClass": "STANDARD",
        },
    ]
    result_data = check.contents_parse(data)
    assert result_data == [
        {
            "Key": "fuga0.txt",
            "LastModified": datetime.datetime(2023, 11, 19, 0, 22, 20, tzinfo=tzutc()),
        },
        {
            "Key": "fuga1.txt",
            "LastModified": datetime.datetime(2023, 11, 19, 0, 22, 20, tzinfo=tzutc()),
        },
        {
            "Key": "fuga2.txt",
            "LastModified": datetime.datetime(2023, 11, 19, 0, 22, 20, tzinfo=tzutc()),
        },
    ]
