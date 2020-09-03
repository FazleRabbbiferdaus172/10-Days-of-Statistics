n = int(input())

x = [int(s) for s in input().split()]

w = [int(s) for s in input().split()]

x_w = [x[i]*w[i] for i in range(n)]

w_mean = sum(x_w)/sum(w)

print("{:.1f}".format(w_mean))
