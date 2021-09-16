def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
r =gcd(2019,324)
print(r)
