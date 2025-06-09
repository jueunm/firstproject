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

# 간단한 키워드 기반 감정 분류
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
    return "좋음"  # 기본값

# 플레이리스트 데이터: (MBTI, 감정카테고리) → 곡 리스트
playlist_data = {
    ("INFP", "우울"): {
        "songs": [
            ("잔나비 - 주저하는 연인들을 위해", "우리의 시간이 멈춘다면 얼마나 좋을까"),
            ("이수현 - 사랑이 아냐", "사랑이란 말로 다 설명할 순 없죠"),
            ("권진아 - 끝", "끝이 나도 마음은 끝나지 않죠"),
            ("적재 - 나랑 같이 걸을래", "그대와 걷는 이 길이 좋아서 그래요")
        ],
        "reason": "감성이 깊은 INFP에게 우울할 때는 따뜻하고 위로되는 곡이 필요해요. 🌧️"
    },
    ("ENFP", "설렘"): {
        "songs": [
            ("아이유 - 너의 의미", "넌 나에게 언제나 설렘을 줘"),
            ("백예린 - 우주를 건너", "나의 마음이 너에게 닿기를"),
            ("볼빨간사춘기 - 썸 탈꺼야", "오늘부터 우리는 사랑을 할 거야"),
            ("세븐틴 - 예쁘다", "그냥 예쁘다, 네가")
        ],
        "reason": "ENFP는 사랑과 감정에 솔직해요! 설렘엔 달달하고 상큼한 노래가 어울려요. 🍓"
    },
    ("INTJ", "지침"): {
        "songs": [
            ("검정치마 - 기다린 만큼, 더", "기다린 만큼 더 멀어지는 것 같아"),
            ("새소년 - 긴 꿈", "어디쯤에서 우린 스쳐갔을까"),
            ("OOHYO - 민들레", "바람결 따라 흩날리는 민들레처럼"),
            ("혁오 - TOMBOY", "꿈 속을 걷는 듯한 이 기분은 뭘까")
        ],
        "reason": "지친 INTJ는 깊은 사색과 위로가 담긴 노래로 내면을 다독일 수 있어요. 🌙"
    },
    ("ISFJ", "좋음"): {
        "songs": [
            ("아이유 - 좋은 날", "오늘은 정말 좋은 날~"),
            ("브라운 아이드 소울 - My Story", "나의 이야기 그대에게 들려줄게요"),
            ("적재 - Love Again", "다시 사랑할 수 있을까"),
            ("폴킴 - 모든 날, 모든 순간", "너를 만나 참 행복했어")
        ],
        "reason": "따뜻한 ISFJ의 밝은 기분엔 감성적이고 사랑스러운 곡들이 잘 어울려요. 🌞"
    },
    ("ENTP", "짜증"): {
        "songs": [
            ("지코 - 아무노래", "그냥 아무 노래나 틀어줘"),
            ("비와이 - Day Day", "나는 오늘도 내 길을 간다"),
            ("DPR LIVE - Text Me", "Don’t be afraid, just text me"),
            ("박재범 - All I Wanna Do", "All I wanna do is kick it with you")
        ],
        "reason": "짜증이 날 땐 ENTP처럼 터트려야죠! 리듬감 있는 곡으로 스트레스 날려요! 💣"
    },
    # fallback
    ("DEFAULT", "DEFAULT"): {
        "songs": [
            ("아이유 - 에필로그", "우린 끝난 걸까, 아니면 시작인 걸까"),
            ("백예린 - 그건 아마 우리의 잘못은 아닐 거야", "모든 건 그대로 흘러갔겠지"),
            ("적재 - 나랑 같이 걸을래", "그대와 걷는 이 길이 좋아서 그래요")
        ],
        "reason": "모든 사람에게 무난하게 어울리는 감성 명곡 모음이에요. 🎧"
    }
}

# 추천 로직 실행
if mbti and mood_input:
    mood_category = classify_mood(mood_input)
    key = (mbti, mood_category)
    result = playlist_data.get(key, playlist_data[("DEFAULT", "DEFAULT")])

    st.balloons()
    st.success(f"🎶 {mbti} + '{mood_input}' 감정 = '{mood_category}' 감정으로 분류되었어요!")
    
    st.markdown(f"💿 **추천 플레이리스트:**")
    for song, lyric in result["songs"]:
        st.markdown(f"- **{song}**  \n  _🎵 “{lyric}”_")

    st.markdown("---")
    st.markdown(f"📌 **추천 이유:** _{result['reason']}_")
