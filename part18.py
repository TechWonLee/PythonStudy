import re
#정규 표현식

# p = re.compile('[a-z]+')
# m = p.match('python')
# print(m)


p = re.compile('[a-z]+')
m = p.search('3 python')
print(m)

 