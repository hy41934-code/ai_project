
        "lon": 127.009224,
        "subway": "동대문역사문화공원역",
        "fun": "야간 산책, 전시회 관람"
    },
    {
        "name": "코엑스",
        "lat": 37.511685,
        "lon": 127.059151,
        "subway": "삼성역(2호선)",
        "fun": "별마당도서관, 아쿠아리움"
    },
    {
        "name": "청계천",
        "lat": 37.569246,
        "lon": 126.978388,
        "subway": "종각역(1호선)",
        "fun": "산책, 야경 감상"
    },
    {
        "name": "이태원",
        "lat": 37.534925,
        "lon": 126.994106,
        "subway": "이태원역(6호선)",
        "fun": "세계 음식 맛집 탐방, 펍 투어"
    }
]

# 서울 중심 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# 관광지 마커 추가
for place in places:
    popup_text = f"""
    <b>{place['name']}</b><br>
    🚇 가까운 역: {place['subway']}<br>
    🎈 놀거리: {place['fun']}
    """

    folium.Marker(
        location=[place['lat'], place['lon']],
        popup=folium.Popup(popup_text, max_width=300),
        tooltip=place['name'],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력
map_data = st_folium(m, width=1000, height=600)

st.markdown("---")
st.subheader("📍 관광지 정보")

# 클릭된 관광지 정보 표시
if map_data and map_data.get("last_object_clicked_popup"):
    popup = map_data["last_object_clicked_popup"]

    st.success(f"{popup.replace('<br>', ' | ').replace('<b>', '').replace('</b>', '')}")
else:
    st.info("지도에서 관광지를 클릭해보세요!")
