data = ([1, 2, 3, 4, 5], 10)

data,s = data
data = data * 2

a = [data[i:i+2] for i in data]

print(a)
b = [j[1] + j[0] for j in a] 

b = list(set(b))
c = [abs(s - k) for k in b]

d = list(zip(b,c))
d = sorted(d, key= lambda x:x[1])
print(d[0][0])


