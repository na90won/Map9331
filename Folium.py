import folium
from pandas import DataFrame   # 데이터 분석 패키지
from pandas import ExcelFile   # 엑셀파일 가져오기

# zoom_start: 배율 1~22
map_osm = folium.Map(location=[37.566647,126.978426], zoom_start=17)
map_osm

# 새로운 지도 객체 생성
map_osm1 = folium.Map(location=[37.566647,126.978426], zoom_start=17)

# 마커 객체 생성
marker1 = folium.Marker([37.566647,126.978426],
                        popup='서울특별시청',
                        icon=folium.Icon(color='red'))

marker1.add_to(map_osm1)  # 마커 객체를 지도에 추가함
map_osm1                  # 지도 표시하기

# 새로운 지도 객체 생성
map_osm2 = folium.Map(location=[37.502549, 127.024867], zoom_start=17)

# HTML을 사용한 팝업
popup_html = folium.Popup("<font color='green' style='white-space: nowrap'><b>이젠아카데미컴퓨터학원</b></font>", parse_html=False)

# 사용자 지정 아이콘 이미지 사용
icon_img = folium.features.CustomIcon('http://itpaper.co.kr/demo/py/ho.png', icon_size=(50, 50))

# 마커 객체 생성
marker2 = folium.Marker([37.502549, 127.024867],
                        popup=popup_html,
                        icon=icon_img)

marker2.add_to(map_osm2) # 마커 객체를 지도에 추가함
map_osm2                 # 지도 표시하기

# 새로운 지도 객체 생성
map_osm3 = folium.Map(location=[37.502549, 127.024867], zoom_start=17)

# 원형마커
marker3 = folium.CircleMarker([37.502549, 127.024867],
                              radius=100,                 # 범위
                              color='#3186cc',            # 선 색상
                              fill_color='#3186cc',       # 면 색상
                              popup='이젠아카데미컴퓨터학원')

marker3.add_to(map_osm3)

map_osm3