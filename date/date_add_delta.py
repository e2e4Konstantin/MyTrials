# import datetime
# from datetime import timedelta, date
# from dateutil.relativedelta import relativedelta

# end_date = date.today() + timedelta(days=5)
# print(date.today(), end_date)



# end_date = date.today() + relativedelta(months=1)

# print(date.today(), end_date)

# date_string = "2024-04-26"
# date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()

# print(date_object, date_object + relativedelta(months=1))


from datetime import datetime
from dateutil.relativedelta import relativedelta

date_string = "2024-04-26"
date_object = datetime.strptime(date_string, "%Y-%m-%d").date()

print(date_object, date_object + relativedelta(months=1))
nd = date_object.strftime("%Y-%m-%d")
print(nd, type(nd))