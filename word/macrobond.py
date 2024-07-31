import win32com.client

c = win32com.client.gencache.EnsureDispatch("Macrobond.Connection")
d = c.Database
s = d.FetchOneSeries("usgdp")

values = s.Values
values2 = tuple(val/1000000000000 for val in values)
print(values2)