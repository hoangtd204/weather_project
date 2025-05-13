import datetime
from zoneinfo import ZoneInfo
from timezonefinder import TimezoneFinder




def format_timezone(raw_timezone):
        timezone_offset = raw_timezone
        utc_offset_hours = timezone_offset / 3600
        return utc_offset_hours

def convert_to_local_sun(raw_data, lat, lon):
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lng=lon, lat=lat)
        if timezone_str:
            sun_utc = datetime.datetime.fromtimestamp(raw_data, tz=datetime.timezone.utc)
            sun_local = sun_utc.astimezone(ZoneInfo(timezone_str))
            return sun_local
        else:
            return "Timezone not found for the given coordinates."

