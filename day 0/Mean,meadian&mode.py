n = int(input())
l = [int(x) for x in input().split()]
l.sort(reverse=True)
mean = sum(l)/n


m = n//2
if n % 2 == 1:
    median = l[m]
else:
    median = sum(l[m-1:m+1])/2

mode = min(l)
max_count = 1
for i in l:
    if max_count <= l.count(i):
        max_count = l.count(i)
        mode = i

print("{:.1f}".format(mean))
print("{:.1f}".format(median))
print(mode)
