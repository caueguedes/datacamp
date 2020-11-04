import datetime
from datetime import timedelta
# https://strftime.org/

datetime.datetime.now()
datetime.datetime.strptime("07/06/91", "%m/%d/%y")
# %A : Wednesday, %B: September, %d: 01, %Y: 1991
birthday = datetime.datetime(1991, 7, 6)
datetime.datetime.strftime(birthday, "%A, %B %d, %Y")

# datetime.[year, month, day, second]
datetime.datetime.now() > datetime.datetime.now()
datetime.datetime.now() - birthday

dt = datetime.datetime(2019, 1, 14, 0, 0)
datetime.datetime(dt.year, dt.month, dt.day - 7)  # 2019 1 7
dt - timedelta(weeks=1)


## Dictionaries