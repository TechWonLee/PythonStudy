try:
    4/0
except Exception as e:
    print(e)
finally:
    print("확인되셨나요?")

def positive(x):
    return x >0

a = list(filter(positive, [1,3,4,5,-1,-2,-3]))
print(a)