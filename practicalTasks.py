
# Find the max number of factor occurences
# region
n = int(input("Enter n: "))
factor = 2
countMax = 0
factorMax = 0
while factor**2 <= n:
    count = 0
    while n % factor == 0:
        count += 1
        n //= factor
    if count >= countMax:
        countMax = count
        factorMax = factor
    if factor == 2:
        factor = 3
    else:
        factor += 2
if n != 1 and countMax <= 1:
    countMax = 1
    factorMax = n

print(countMax)

# endregion


# how many 3-digit primes exist that only have odd digits
# region
count = 0
for p in range(100, 1000):
    if p % 2 == 0 or (p // 10) % 2 == 0 or (p // 100) % 2 == 0:
        continue

    factor = 2


# endregion


# simplified and unsimplified form
# region
a = int(input("Enter a: "))
b = int(input("Enter b: "))

x = a
y = b

while b > 0:
    x, y = x, y % x
print(a, "/", b)
print(a // x, '/', b//x)


# endregion