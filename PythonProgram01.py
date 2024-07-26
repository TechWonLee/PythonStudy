fruit = ["딸기", "사과", "바나나", "바나나", "복숭아"]

d = {}

for f in fruit:
    if f in d: #딸기 라는 key가 d라는 딕셔너리에 들어있는지
        d[f] = d[f] + 1
    else:
        d[f] = 1 #딸기 애가 없으면 딕셔너리에 넣고 벨류는 1로 만들어줘

print(d)

#프로그램 설명 : 리스트값들의 값을 키 값으로 딕셔너리에 삽입하고, value값을 동일한 키값이 있을때를 체크해서 갯수를 세는 프로그램이다. 


Test = ["하이","하이2","하이3"]

s = {}
for a in Test:
   if a in s:
       s[a] = s[a] + 1
       print(s[a])
   else:
       s[a] = 1
       print(s[a])
       

print(s)