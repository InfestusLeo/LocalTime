from geopy import geocoders
from datetime import datetime
from timezonefinder import TimezoneFinder as TzF
from pytz import timezone

class LocalTime():
    def time(self, city: str):
        g = geocoders.GoogleV3()
        (latitude, longitude) = g.geocode(city)[1]
        tf = TzF()
        dt_format = "%I:%M %p"
        time = datetime.now(timezone(tf.closest_timezone_at(lng = longitude, lat = latitude))).strftime(dt_format)
        return time