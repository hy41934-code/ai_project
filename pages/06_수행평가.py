import streamlit as st
import pandas as pd
import random

# 페이지 설정
st.set_page_config(
    page_title="대구 북구 관광지 추천",
    page_icon="🗺️",
    layout="centered"
)

# 데이터 불러오기
df = pd.read_csv("tour.csv", encoding="utf-8")

st.title("🗺️ 대구 북구 관광지 추천기")
st.write("관광지 종류를 선택하면 추천 장소를 알려줄게! 😎")

# 관광종류 목록
types = sorted(df["관광종류"].dropna().unique())

selected_type = st.selectbox(
    "🎯 어떤 종류의 관광지를 찾고 있니?",
    types
)

# 추천 이유
reason_dict = {
    "체험관광": "직접 참여하면서 특별한 추억을 만들 수 있어! 🎨",
    "전통시장": "맛있는 먹거리와 활기찬 분위기를 즐길 수 있어! 🍢",
    "문화예술공간": "감성 충전하기 좋은 장소야! 🎭",
    "자연관광": "푸른 자연을 보며 힐링하기 좋아! 🌳",
    "북구8경": "북구를 대표하는 멋진 명소들이야! 📸",
    "북구의길": "산책하며 여유를 즐기기 좋아! 🚶",
    "옥산로 테마거리": "특색 있는 거리 분위기를 느낄 수 있어! ✨",
    "기타": "숨겨진 매력이 있는 장소들이야! 😆"
}

if st.button("✨ 추천 받기"):
    filtered = df[df["관광종류"] == selected_type]

    if len(filtered) == 0:
        st.warning("추천할 관광지가 없어 😢")
    else:
        sample_size = min(2, len(filtered))
        recommendations = filtered.sample(sample_size)

        st.success("🎉 오늘의 추천 관광지!")

        for i, (_, row) in enumerate(recommendations.iterrows(), start=1):
            st.subheader(f"📍 추천 {i}. {row['관광지명']}")

            st.write(f"🏠 주소 : {row['주소']}")

            if pd.notna(row["입장료"]):
                st.write(f"💰 입장료 : {row['입장료']}")

            st.write(
                f"👉 추천 이유 : {reason_dict.get(selected_type, '한 번쯤 가볼 만한 멋진 장소야! 😄')}"
            )

            st.divider()

st.markdown("---")
st.caption("💙 대구 북구 관광지 데이터를 활용한 추천 서비스")
