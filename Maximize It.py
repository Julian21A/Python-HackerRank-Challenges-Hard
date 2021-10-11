import itertools as it

c,o=list(map(int,input().split()))
combinaciones = []
for i in range(c):
    combinaciones.append(map(lambda x: x**2, map(int,input().strip().split()[1:])))
print (max(map(lambda x: x % o, map(sum, it.product(*combinaciones)))))
