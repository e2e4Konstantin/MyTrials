import time
from datetime import datetime, timezone
import calendar


# для получения временной метки в секундах с момента наступления эпохи.
print(time.time())

# UTC+1, time.time() и datetime.utcnow().timestamp() не дают одного и того же значения!
# Если вы получаете эту временную метку, чтобы использовать ее в другой системе,
# которая ожидает настоящую истинную Unix-временную метку времени Epoch,
# то лучше использовать datetime.now().timestamp(), иначе произойдет смещение.

print(datetime.utcnow().timestamp())

# Это неправильный ответ. datetime.utcnow().timestamp() возвращает неверный результат,
# если только вы не находитесь в UTC+00 tz. datetime.now().timestamp() является правильным
print(datetime.now().timestamp())


d = datetime.utcnow()
unixtime = calendar.timegm(d.utctimetuple())
print(unixtime)


print(datetime(1970, 1, 1, 1, 0, tzinfo=timezone.utc).timestamp())
print(datetime.fromisoformat("1970-01-01T01:00:00+00:00").timestamp())

print(int(datetime.now(tz=timezone.utc).timestamp() * 1000))
print(datetime.utcnow())

dts = datetime.utcnow()
epochtime = round(time.mktime(dts.timetuple()) + dts.microsecond / 1e6)
print(epochtime)
