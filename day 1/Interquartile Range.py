def find_median(n, l):
    m = n//2
    if n % 2 == 1:
        median = l[m]
    else:
        median = sum(l[m-1:m+1])/2

    return median, m


n = int(input())

l = [int(x) for x in input().split()]
f = [int(x) for x in input().split()]
la = []

for i in range(n):
    x = [l[i]]*f[i]
    la += x

la.sort()

q2, m = find_median(len(la), la)

if n % 2 == 1:
    q1, a = find_median(len(la[:m]), la[:m])
    q3, a = find_median(len(la[m+1:]), la[m+1:])

else:
    q1, a = find_median(len(la[:m]), la[:m])
    q3, a = find_median(len(la[m:]), la[m:])


print("{:.1f}".format(abs(q3-q1)))
