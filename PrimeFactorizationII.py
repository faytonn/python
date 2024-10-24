n = int(input())

factor = 2
result = ''


while factor ** 2 <= n:
    count = 0
    while n % factor == 0:
        n //= factor
        count += 1
    if count > 0:
        if count == 1:
            result += str(factor) + ' * '
        else:
            result += str(factor) + '^' + str(count) + ' * '
        
    if factor == 2:
        factor = 3
    else:
        factor += 2
        
if n > 1:
    result += str(n)
    
if result.endswith(' * '):
    result = result[: -3]
    
print(result)