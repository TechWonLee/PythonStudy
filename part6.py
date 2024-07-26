## 제어문(조건문, 반복문)

money = 1000
if money < 3000:
    print("택시타라 임마")
    print("네네 선장님!")
else:
    print("걸어가라 임마")




if 1 in [1,2,3]:
    # pass - 지나가라 라는 뜻
    print("기차 타고 가라 임마")
    
else:
    print("걸어가라 임마")

score = 70
message = "success" if score >= 60 else "failure"
# 3항 연산자와 같음
print(message)

