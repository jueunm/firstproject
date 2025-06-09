import streamlit as st
import pandas as pd

# CSV 불러오기
df = pd.read_csv("playlist_data_full.csv")

# 감정 분류 함수
def classify_emotion(text):
    text = text.lower()
    if any(word in text for word in ["슬퍼", "우울", "눈물", "속상", "외로"]):
        return "우울"
    elif any(word in text for word in ["설레", "두근", "기대", "좋아하는", "사랑"]):
        return "설렘"
    elif any(word in text for word in ["힘들", "지쳐", "피곤", "졸려", "지침"]):
        return "지침"
    elif any(word in text for word in ["좋아", "기뻐", "행복", "신나", "즐거"]):
        return "좋음"
    elif any(word in text for word in ["짜증", "화나", "열받", "스트레스", "답답"]):
        return "짜증"
    else:
        return "좋음"  # 기본값

# 감정별 배경색
background_colors = {
    "우울": "#dbeafe",  # 연파랑
    "설렘": "#fce7f3",  # 연핑크
    "지침": "#fef9c3",  # 연노랑
    "좋음": "#dcfce7",  # 연초록
    "짜증": "#fee2e2"   # 연빨강
}

# 사용자 입력
st.title("🎧 MBTI & 감정 기반 한국 노래 추천기")
mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", sorted(df["mbti"].unique()))
emotion_input = st.text_input("지금 기분은 어떤가요? 😌 (예: 기분 좋아요, 좀 힘들어요 등)")

if emotion_input:
    emotion = classify_emotion(emotion_input)
    bg_color = background_colors.get(emotion, "#ffffff")

    # 배경색 스타일 적용
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {bg_color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # 필터링
    filtered = df[(df["mbti"] == mbti) & (df["emotion"] == emotion)]

    if not filtered.empty:
        st.balloons()
        st.subheader(f"✨ {mbti} + {emotion} 기분에 어울리는 플레이리스트 🎶")

        for _, row in filtered.iterrows():
            # 유튜브 썸네일 이미지 URL 추출
            video_id = row["youtube_url"].split("v=")[1].split("&")[0]
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"

            # 카드 스타일 출력
            with st.container():
                cols = st.columns([1, 3])
                with cols[0]:
                    st.image(thumbnail_url, use_container_width=True)
                with cols[1]:
                    st.markdown(f"""
                    **🎵 {row['song_title']}**  
                    _"{row['lyric_line']}"_  
                    [▶️ 유튜브에서 듣기]({row['youtube_url']})  
                    """)
        # 추천 이유 (대표 한 곡 기준)
        st.markdown(f"💡 추천 이유: {filtered.iloc[0]['reason']}")

    else:
        st.warning("앗! 조건에 맞는 노래가 아직 준비되지 않았어요 😢")
