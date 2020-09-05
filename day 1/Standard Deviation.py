n = int(input())
l = [int(x) for x in input().split()]

mean = sum(l)/n

la = [(i-mean)**2 for i in l]

print("{:.1f}".format((sum(la)/n)**.5))
