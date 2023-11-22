
l = [str(x) for x in range(50) if x%2 == 0]
print(l)

x = []
field = []
n = [x.extend(field) for line in open("num.txt") if line.strip() and (field := line.strip().split())]
print(x)

n = [line.strip().split() for line in open("num.txt") if line.strip()]
print(n)

n = sum([float(nums) for line in open("num.txt") if line.strip() for nums in line.strip().split()])
print(n)

d = ['0', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32', '34', '36']
dl = [
    int(x)
    for x in d
    if int(x) > 10 if int(x) < 30
]
print(dl)



