import time
from datetime import timedelta
start_time = time.monotonic()
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))