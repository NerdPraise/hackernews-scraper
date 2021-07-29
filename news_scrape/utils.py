import datetime
from django.utils import timezone
def unix_to_datetime(unixtime):
    dt = datetime.datetime.fromtimestamp(int(unixtime))
    tz_dt = timezone.make_aware(dt, timezone.get_default_timezone())
    return tz_dt

