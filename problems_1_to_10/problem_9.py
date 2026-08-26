from math import ceil, gcd, sqrt

# This solution uses the fact that a Pythagorean triplet, (a,b,c), with a and b having
# different parity, is of the form (2mn, m^2-n^2, m^2+n^2) if gcd(a,b) = gcd(b,c) = gcd(a,c) = 1.
# Otherwise, it is of the form  (2mn*d, (m^2-n^2)*d, (m^2+n^2)*d) where gcd(a,b) = gcd(b,c) = gcd(a,c) = d
# Thus, we conclude that if a + b + c = S, then 2m(m+n)d = S

s = 1_000

s_over2 = s // 2
max_m = ceil(sqrt(s))
max_mult = -1
curr_mult = 1
for m in range(2, max_m):
    if s_over2 % m == 0:
        s_over_2m = s_over2 // m

        lower_limit = m + m % 2 + 1
        upper_limit = min(2 * m, s_over_2m)
        for k in range(lower_limit, upper_limit, 2):
            if s_over_2m % k == 0 and gcd(m, k) == 1:
                d = s_over2 // (k *m)
                n = k - m
                a = 2 * m * n * d
                b = (m ** 2 - n ** 2) * d
                c = (m ** 2 + n ** 2) * d
                curr_mult = a * b * c
                max_mult = max(max_mult, curr_mult) 

print(max_mult)