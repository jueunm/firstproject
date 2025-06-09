import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 감정 기반 K-POP 추천 🎶", page_icon="🎤", layout="centered")

st.title("🎤 MBTI × 감정 기반 K-POP 플레이리스트")
st.markdown("지금 기분을 말해줘요. 당신의 MBTI와 기분에 딱 맞는 노래를 추천해줄게요! 💌")

# MBTI 선택
mbti_types = [
    "INTP", "INTJ", "ENTP", "INFJ", "ENFP", "ISTJ", "ISFJ",
    "ESTJ", "ESFJ", "ENTJ", "ISTP", "ISFP", "ESTP", "ESFP", "INFP", "ENFJ"
]
mbti = st.selectbox("🧬 당신의 MBTI는?", options=mbti_types)

# 감정 입력
mood_input = st.text_input("🧠 지금 기분을 자유롭게 표현해보세요 (예: 기운이 없고 우울해요...)")

# 감정 분류 함수
def classify_mood(text):
    mood_keywords = {
        '우울': ['우울', '슬퍼', '눈물', '힘들', '속상', '외로', '죽고', '아파', '지쳐'],
        '설렘': ['설레', '두근', '좋아', '사랑', '떨려', '기대'],
        '지침': ['지쳐', '피곤', '힘들', '무기력', '탈진', '현타'],
        '좋음': ['행복', '좋아', '기분 짱', '즐거워', '신나', '상쾌', '평온'],
        '짜증': ['짜증', '화나', '열받', '싫어', '짜증나', '답답']
    }
    for category, keywords in mood_keywords.items():
        if any(kw in text for kw in keywords):
            return category
    return "좋음"

# 배경색 설정 함수
def set_background_color(mood_category):
    bg_colors = {
        '우울': '#D3D3D3',   # 연회색
        '설렘': '#FFE0F0',   # 핑크빛
        '지침': '#B0C4DE',   # 라이트 스틸 블루
        '좋음': '#FFFACD',   # 연노랑
        '짜증': '#FFCCCB',   # 연빨강
    }
    color = bg_colors.get(mood_category, '#FFFFFF')
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 플레이리스트 데이터
playlist_data = {
    ("INFP", "우울"): {
        "songs": [
            ("잔나비 - 주저하는 연인들을 위해", "우리의 시간이 멈춘다면 얼마나 좋을까", "https://www.youtube.com/watch?v=7T4KHxS-K7U"),
            ("이수현 - 사랑이 아냐", "사랑이란 말로 다 설명할 순 없죠", "https://www.youtube.com/watch?v=dd3K3UqgkY8"),
            ("권진아 - 끝", "끝이 나도 마음은 끝나지 않죠", "https://www.youtube.com/watch?v=8yB2LjgkQ0Y")
        ],
        "reason": "감성이 깊은 INFP에게 우울할 땐 따뜻하고 위로되는 곡이 필요해요. 🌧️"
    },
    ("ENFP", "설렘"): {
        "songs": [
            ("아이유 - 너의 의미", "넌 나에게 언제나 설렘을 줘", "https://www.youtube.com/watch?v=i_cVJgIz_Cs"),
            ("백예린 - 우주를 건너", "나의 마음이 너에게 닿기를", "https://www.youtube.com/watch?v=lYu6Z9vG4CA"),
            ("세븐틴 - 예쁘다", "그냥 예쁘다, 네가", "https://www.youtube.com/watch?v=9M7k9ZV67c0")
        ],
        "reason": "ENFP는 사랑과 감정에 솔직해요! 설렘엔 달달하고 상큼한 노래가 어울려요. 🍓"
    },
    ("INTJ", "지침"): {
        "songs": [
            ("혁오 - TOMBOY", "꿈 속을 걷는 듯한 이 기분은 뭘까", "https://www.youtube.com/watch?v=2i2khp_npdE"),
            ("새소년 - 긴 꿈", "어디쯤에서 우린 스쳐갔을까", "https://www.youtube.com/watch?v=CO4ONe-oePA"),
            ("검정치마 - 기다린 만큼, 더", "기다린 만큼 더 멀어지는 것 같아", "https://www.youtube.com/watch?v=bc1zW2hLSC4")
        ],
        "reason": "지친 INTJ는 사색과 위로가 담긴 노래로 내면을 다독일 수 있어요. 🌙"
    },
    ("DEFAULT", "DEFAULT"): {
        "songs": [
            ("아이유 - 에필로그", "우린 끝난 걸까, 아니면 시작인 걸까", "https://www.youtube.com/watch?v=d1NIdN5p5fU"),
            ("백예린 - 그건 아마 우리의 잘못은 아닐 거야", "모든 건 그대로 흘러갔겠지", "https://www.youtube.com/watch?v=wTzF2Wcfz_E"),
            ("적재 - 나랑 같이 걸을래", "그대와 걷는 이 길이 좋아서 그래요", "https://www.youtube.com/watch?v=UKhFZ8T3ISg")
        ],
        "reason": "모든 사람에게 무난하게 어울리는 감성 명곡 모음이에요. 🎧"
    }
}

# 입력이 모두 주어졌을 때 실행
if mbti and mood_input:
    mood_category = classify_mood(mood_input)
    set_background_color(mood_category)
    key = (mbti, mood_category)
    result = playlist_data.get(key, playlist_data[("DEFAULT", "DEFAULT")])

    st.balloons()
    st.success(f"🎶 {mbti} + '{mood_input}' 감정 → **'{mood_category}'** 감정으로 분류되었어요!")

    st.markdown("💿 **추천 플레이리스트:**")
    for song, lyric, youtube_url in result["songs"]:
        st.markdown(f"- **{song}**  \n  _🎵 “{lyric}”_  \n  [▶️ 유튜브 바로가기]({youtube_url})")

    st.markdown("---")
    st.markdown(f"📌 **추천 이유:** _{result['reason']}_")
