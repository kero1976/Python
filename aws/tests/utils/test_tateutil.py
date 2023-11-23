from aws.utils import dateutil
import datetime
from dateutil.tz import tzutc


def test_to_str():
    dt = datetime.datetime(2023, 11, 22, 23, 1, 43, tzinfo=tzutc())
    response = dateutil.to_str(dt)
    assert response == "2023/11/22 23:01:43"
