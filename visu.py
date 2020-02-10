import matplotlib.pyplot as plt

with open('data.csv', 'r') as f:
    res = [[],[]]
    for i in range(1):
        f.readline()
    for line in f:
        line = line.rstrip()
        words = line.split(',')
        # res[0].append(int(words[0]))
        # res[1].append(int(words[1]))
        res.append([ float(words[0]),float(words[1]) ])


print(len(res[0]))
print(len(res[1]))
plt.plot(res[0], res[1], 'ro')
plt.axis([0, 250000, 0, 9000])
plt.xlabel("kilometers")
plt.ylabel("price")
plt.show()