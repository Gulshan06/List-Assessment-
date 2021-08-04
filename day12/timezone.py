import pytz
from datetime import datetime

standrad_time=pytz.utc
time_zone = pytz.timezone("Africa/Abidjan")
# time_zone = pytz.timezone("	Africa/Addis_Ababa")
print(datetime.now(standrad_time))
print(datetime.now(time_zone))