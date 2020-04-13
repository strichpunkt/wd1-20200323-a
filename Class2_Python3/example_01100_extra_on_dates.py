import datetime

birthdate = datetime.datetime(1987, 1, 1)           # datetime object
elapsed = datetime.datetime.now() - birthdate       # timedelta object
print(elapsed.total_seconds())                      # float
print(birthdate + datetime.timedelta(days=20000))   # datetime

print("date today:", datetime.date.today())
print("time now:", datetime.datetime.now())
print("time now (iso):", datetime.datetime.now().isoformat())

today = datetime.datetime.today()
birthdate = datetime.datetime(1990, 1, 1)
difference = today - birthdate
print(difference.total_seconds())
