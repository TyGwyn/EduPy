orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
s = list(map(lambda a:(a[0]!=a[1])* 3.14  * a[0]* a[1], orbits))
print(max(orbits, key = lambda a:(a[0]!=a[1])* 3.14 * a[0] * a[1]))


