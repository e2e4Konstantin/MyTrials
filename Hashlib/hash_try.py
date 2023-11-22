import hashlib
import binascii

s = "Нагнетание раствора за  сборную чугунную обделку тоннелей, сооружаемых без щита, при притоке воды в забое более 5 м3/ч в грунтах 4-5 групп диаметр 5,5 м-6,0 м"
# st = "hello world"

# sb1 = st.encode('ascii')
# print(sb1)
# h = hashlib.md5(sb1).hexdigest()
# print(h)

s_bytes = bytes(s, "utf8")
print(type(s_bytes), len(s_bytes))

sb2 = s.encode("utf8")
print(type(sb2), len(sb2))
# print(sb2)
h = hashlib.sha256(sb2).hexdigest()
h1 = hashlib.sha256(s_bytes).hexdigest()
print(h, h1, bool(h == h1))


# m = hashlib.sha256()
# m.update(b"Nobody inspects")
# m.update(b" the spammish repetition")
# print(m.digest())
hr = hashlib.new("SHA256")
print(hr)
hr.update(s.encode("utf8"))
print(hr.digest())
print(hr.hexdigest())
