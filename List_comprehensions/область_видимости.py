import dis

x = 100
for i in range(3):
    x = i * 5
print(x)

x = 100
j = [x * 5 for x in range(3)]
print(x)


def gloop():
    x = 100
    for i in range(3):
        x = i * 5

def lcloop():
    x = 100
    print([x * 5 for x in range(3)])



print(dis.dis(gloop))
print('------------------')
print(dis.dis(lcloop))