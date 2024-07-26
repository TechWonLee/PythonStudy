treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무넘어간데이~~")


coffee = 10
money = 300
while money:
    print("돈받았으니 커피드림.")
    coffee = coffee-1
    print("남은 커피양은 %d 입니다." %coffee) 
    if not coffee: #0은 false 인데 not 이 붙어서 true가되어 if문이 실행됨
        print("커피 다떨어짐 칼퇴욥~~ ")
        break

#a=0
#while a <10:
#    a = a+1
#    if a % 2 ==0:
#        continue
#    print(a)
    

bb = [(1,2), (3,4), (5,6)]
for(first, last) in bb:
    print(first)
    print(last)


marks = [90, 25, 76, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >=60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다 아쉽네요 ㅠ_ㅠ" %number)




sum = 0 
for i in range(1, 101): ##(이상~~, 미만.)
    sum = sum+i
print(sum)


for i in range (2, 10):
    for j in range(1,10):
      print(i*j, end=" ")
    print('')