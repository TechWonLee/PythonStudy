def GuGu(n):
    result = []
    i =1
    while i < 10:
        result.append(n*i)
        i= i+1
    return result


print(GuGu(2))

result1=0

for n in range(1,1000):
    if n % 3 == 0 or n % 5 ==0:
        result1 += n

print(result1)