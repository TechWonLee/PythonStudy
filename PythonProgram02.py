#패키지(폴더의 이름이 패키지 이름임) = 라이브러리
#패키지 = 모듈 + 모듈(기능을 구현해 놓은 것)

# animal package
# dog, cat module
# dog, cat module can say "hi"

print(f"__init__.py 경로: {__file__}")
from animal import cat
from animal import dog

d = dog.Dog()
c = cat.Cat()

d.hi()
c.hi()


import sys
print(sys.executable)  # 현재 사용 중인 파이썬 인터프리터 경로 출력

from geopy.geocoders import Nominatim

test = "구로구 디지털로 27"
print(test)

geolocator = Nominatim(user_agent='Korea')
location = geolocator.geocode(test)

if location:
    latitude = location.latitude
    longitude = location.longitude
    print(f"Latitude: {latitude}, Longitude: {longitude}")
else: print('파일 위치를 찾을 수 없습니다.')
