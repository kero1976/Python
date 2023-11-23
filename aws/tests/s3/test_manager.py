from aws.s3 import manager
from moto import mock_s3
import boto3
import datetime
from dateutil.tz import tzutc


def test_get_list_ng():
    response = manager.get_list("foo")
    assert response is None


def test_get_list_ok():
    with mock_s3():
        conn = boto3.resource("s3", region_name="us-east-1")
        conn.create_bucket(Bucket="foo")
        bucket = conn.Bucket("foo")
        bucket.upload_file(__file__, "fuga.txt")
        response = manager.get_list("foo")
    # 時刻の確認ができないので、完全一致ではなく、部分一致で確認している
    # [{'Key': 'fuga.txt', 'LastModified': datetime.datetime(2023, 11, 22, 22, 58, 38, tzinfo=tzutc())}]
    print("■" * 100)
    LastModified = response[0].get("LastModified")
    print(LastModified)
    print(type(LastModified))
    assert response[0].get("Key") == "fuga.txt"
