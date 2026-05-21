# Streamlit 서울시 행정구별 인구수 대시보드

## app.py

```python
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 페이지 설정
st.set_page_config(page_title="서울시 행정구별 인구수", layout="wide")

st.title("서울시 행정구별 인구수")

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 불러오기
@st.cache_data

def load_data():
    df = pd.read_csv('population.csv', encoding='cp949')

    # 숫자형 변환
    for col in df.columns[1:]:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(',', '', regex=False)
        )
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df


df = load_data()

# 구 데이터만 필터링
city_df = df[df['행정구역'].str.contains('구')].copy()

# 선택 가능한 구 목록
selected_gu = st.selectbox(
    '행정구를 선택하세요',
    city_df['행정구역'].tolist()
)

# 선택된 데이터
selected_data = city_df[city_df['행정구역'] == selected_gu].iloc[0]

# 연령대 컬럼
age_columns = [
    '2026년04월_거주자_0~9세',
    '2026년04월_거주자_10~19세',
    '2026년04월_거주자_20~29세',
    '2026년04월_거주자_30~39세',
    '2026년04월_거주자_40~49세',
    '2026년04월_거주자_50~59세',
    '2026년04월_거주자_60~69세',
    '2026년04월_거주자_70~79세',
    '2026년04월_거주자_80~89세'
]

# 그래프용 데이터 생성
ages = [col.split('_')[-1] for col in age_columns]
populations = [selected_data[col] for col in age_columns]

# 그래프 생성
fig, ax = plt.subplots(figsize=(10, 5))

# 회색 배경
fig.patch.set_facecolor('lightgray')
ax.set_facecolor('lightgray')

# 빨간색 꺾은선 그래프
ax.plot(
    ages,
    populations,
    color='red',
    marker='o',
    linewidth=3
)

# 제목 및 라벨
ax.set_title('서울시 행정구별 인구수', fontsize=18)
ax.set_xlabel('나이', fontsize=12)
ax.set_ylabel('인구수', fontsize=12)

# 격자
ax.grid(True, linestyle='--', alpha=0.5)

# Streamlit 출력
st.pyplot(fig)
```

---

## requirements.txt

```txt
streamlit
pandas
matplotlib
```

---

## Streamlit Cloud 업로드 방법

1. GitHub 저장소 생성
2. 아래 파일 업로드

   * app.py
   * population.csv
   * requirements.txt
3. Streamlit Cloud 접속
4. GitHub 저장소 연결
5. app.py 선택 후 배포
