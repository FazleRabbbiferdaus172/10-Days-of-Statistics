# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_median(n, l):
    m = n//2
    if n % 2 == 1:
        median = l[m]
    else:
        s = sum(l[m-1:m+1])
        if s % 2 == 1:
            median = s/2
        else:
            median = s//2

    return median, m


n = int(input())

l = [int(x) for x in input().split()]
l.sort()

q2, m = find_median(n, l)

if n % 2 == 1:
    q1, a = find_median(len(l[:m]), l[:m])
    q3, a = find_median(len(l[m+1:]), l[m+1:])

else:
    q1, a = find_median(len(l[:m]), l[:m])
    q3, a = find_median(len(l[m:]), l[m:])


print(q1)
print(q2)
print(q3)
