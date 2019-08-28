def mmc(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numer, denom):
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    if reduced_den == 1:
        return "%d 1" % (reduced_num)
    elif common_divisor == 1:
        return "%d %d" % (numer, denom)
    else:
        return "%d %d" % (reduced_num, reduced_den)

a,b,c,d = map(float, input().split())

divisor = mmc(b,d)

dividendo = ((divisor/b)*a) + ((divisor/d)*c)

print(simplify_fraction(dividendo,divisor))

