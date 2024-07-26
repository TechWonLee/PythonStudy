# f = open("파이썬 새파일.txt", 'w') =>싹 갈아엎고 새로만듬.
# w대신 a(add)로 하면 추가됨.
# for i in range(1, 11):
#     data = "%d번째 줄입니다 \n" %i
#     f.write(data)
# f.close()

# f = open("파이썬 새파일.txt", 'r', encoding="UTF-8")
# line = f.readline() #readline => 한줄 씩  읽어옴.
# print(line)
# f.close()  #=> 항상 close해주는게 좋음. 한줄씩 읽어옴

# f = open("파이썬 새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# f = open("파이썬 새파일.txt", 'r')
# lines = f.readlines()
# for line in lines:
#    print(line, end="") #=> \n을 없애버림.
# f.close()


