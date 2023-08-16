# System
import datetime
import pytz


def get_now(tz="UTC"):
    """
    Return datetime in tz
    """
    if tz == "UTC":
        return datetime.datetime.now(datetime.timezone.utc)

    assert tz in pytz.all_timezones

    return datetime.datetime.now(pytz.timezone(tz))
