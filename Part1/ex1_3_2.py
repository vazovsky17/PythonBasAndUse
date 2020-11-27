# просто по формуле C(n, k) = C(n - 1, k) + C(n - 1, k - 1)
# если второе число меньше, то 0, если второе число 0, то 1
from math import factorial as f
n, k = map(int, input().split())


def mnoz(n, k):
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return 1 if k == 0 else mnoz(n-1, k)+mnoz(n-1, k-1)

'''
решение через факториал
n, k = n, k = map(int, input().split())
u = (f(n)/f(n)*f(n-k))
print(int(u))
'''

print(mnoz(n, k))
