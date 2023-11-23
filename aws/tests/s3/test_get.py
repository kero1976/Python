from aws.s3 import get
from moto import mock_s3
import boto3
import pytest
import botocore


def test_get_client():
    result = get.get_client()
    print(type(result))
    assert result is not None


def test_get_filepath_list():
    with mock_s3():
        conn = boto3.resource("s3", region_name="us-east-1")
        conn.create_bucket(Bucket="foo")
        bucket = conn.Bucket("foo")
        for i in range(3):
            bucket.upload_file(__file__, f"fuga{i}.txt")
        result = get.get_filepath_list(get.get_client(), "foo")
    assert result is not None


def test_get_filepath_list_error():
    with mock_s3():
        conn = boto3.resource("s3", region_name="us-east-1")
        conn.create_bucket(Bucket="foo2")
        client = get.get_client()
        with pytest.raises(Exception) as e:
            get.get_filepath_list(client, "foo")

        # エラーメッセージを検証
        print(type(e.value))
        assert type(e.value) is client.exceptions.NoSuchBucket
