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
    ("ISFP", "좋음"): {
        "songs": [
            ("AKMU - 200%", "널 좋아해요, 정말로", "https://www.youtube.com/watch?v=0Oi8jDMvd_w"),
            ("볼빨간사춘기 - 썸 탈꺼야", "이젠 너랑 썸 탈 거야", "https://www.youtube.com/watch?v=tXV7dfvSefo"),
            ("에릭남 - Love Die Young", "내 사랑은 아직 끝나지 않았어", "https://www.youtube.com/watch?v=ZLslVF2Kyy4")
        ],
        "reason": "감성을 즐기는 ISFP에겐 밝은 무드의 사랑 노래가 잘 어울려요! 🌞"
    },
    ("ENTP", "짜증"): {
        "songs": [
            ("지코 - 아무노래", "그냥 아무 노래나 틀어", "https://www.youtube.com/watch?v=UuV2BmJ1p_I"),
            ("송민호 - 아낙네", "이 세상이 날 가만두질 않아", "https://www.youtube.com/watch?v=cMTAUr3Nm6I"),
            ("비와이 - Forever", "쉴 틈 없이 달려가", "https://www.youtube.com/watch?v=s0-RdJd_T_A")
        ],
        "reason": "짜증나는 날엔 ENTP의 텐션을 유지할 수 있는 박력 있는 비트가 최고! 🔥"
    },
    ("ISTJ", "우울"): {
        "songs": [
            ("정승환 - 너였다면", "그땐 나일 수 있을까", "https://www.youtube.com/watch?v=ddI6sfJ1e-Y"),
            ("윤하 - 사건의 지평선", "너를 보내는 그 순간에도", "https://www.youtube.com/watch?v=YedG2r3qNaM"),
            ("김나영 - 솔직하게 말해서 나", "이젠 너를 놓아줄게", "https://www.youtube.com/watch?v=2qLQRSQrFe0")
        ],
        "reason": "조용히 감정을 곱씹는 ISTJ에게 서정적인 이별 노래는 깊은 울림을 줘요. 🍂"
    },
    ("ESFP", "설렘"): {
        "songs": [
            ("청하 - 롤러코스터", "내 맘은 롤러코스터", "https://www.youtube.com/watch?v=ZMjg5jJlQJM"),
            ("레드벨벳 - 러시안 룰렛", "심장이 뛰는 대로 널 사랑해", "https://www.youtube.com/watch?v=QslJYDX3o8s"),
            ("트와이스 - CHEER UP", "Cheer up baby~ 좀 더 힘을 내", "https://www.youtube.com/watch?v=c7rCyll5AeY")
        ],
        "reason": "ESFP의 활기찬 설렘엔 댄스와 팝의 중독성 강한 곡이 찰떡! 💃"
    },
    ("ENFJ", "좋음"): {
        "songs": [
            ("태연 - 들리나요", "그대만 보여요", "https://www.youtube.com/watch?v=6fC2Z1ehsK8"),
            ("헤이즈 - 비도 오고 그래서", "생각이 나서 그랬던 거야", "https://www.youtube.com/watch?v=TA5OFS_xX0c"),
            ("에피톤 프로젝트 - 나는 그 사람이 아프다", "내가 사랑하는 사람이니까", "https://www.youtube.com/watch?v=RBpMfLa3_jk")
        ],
        "reason": "타인을 따뜻하게 감싸는 ENFJ의 행복은 감성적인 분위기에서 더 빛나요. 🌈"
    },
    ("ISTP", "짜증"): {
        "songs": [
            ("창모 - METEOR", "난 별에서 온 그 남자", "https://www.youtube.com/watch?v=H3D5DY1R4sY"),
            ("이영지 - 낮 밤", "다 부숴버릴 거야", "https://www.youtube.com/watch?v=U44zF6Qczm0"),
            ("비오 - LOVE me", "날 사랑해줘 그냥", "https://www.youtube.com/watch?v=-qf-Sq8ar4k")
        ],
        "reason": "짜증나는 ISTP에게는 직설적이고 시원한 랩곡이 스트레스 해소에 딱! 💥"
    },
    ("ISFJ", "지침"): {
        "songs": [
            ("정은지 - 너란 봄", "그대라는 봄이 와", "https://www.youtube.com/watch?v=Ik2J2LuPVk8"),
            ("크러쉬 - 잊어버리지마", "나를 잊지 말아요", "https://www.youtube.com/watch?v=RWuxs3tPFDY"),
            ("10cm - 봄이 좋냐", "봄이 그렇게도 좋냐 바보야", "https://www.youtube.com/watch?v=qdApMi5PKe0")
        ],
        "reason": "지친 ISFJ에게 잔잔하면서도 마음을 어루만지는 곡이 필요해요. 🌱"
    },
    ("ESTP", "좋음"): {
        "songs": [
            ("싸이 - 강남스타일", "오~오~오~오~", "https://www.youtube.com/watch?v=9bZkp7q19f0"),
            ("제시 - NUNU NANA", "I’m so bad bad", "https://www.youtube.com/watch?v=tDukIfFzX18"),
            ("이효리 - U-Go-Girl", "넌 나를 원해", "https://www.youtube.com/watch?v=09R8_2nJtjg")
        ],
        "reason": "파티피플 ESTP의 기분 좋은 날은 에너지 넘치는 노래로 신나게! 🎉"
    },
    ("INFJ", "우울"): {
        "songs": [
            ("김필 - 어느 날 머리에서 뿔이 자랐다", "이젠 내가 널 지켜줄게", "https://www.youtube.com/watch?v=dWW7HmfUZGU"),
            ("로이킴 - 이기주의보", "넌 내게 상처만 줘", "https://www.youtube.com/watch?v=rJ6ICzZ9h8Q"),
            ("박효신 - 야생화", "다시 피는 야생화처럼", "https://www.youtube.com/watch?v=w3i1TL5p5Ow")
        ],
        "reason": "INFJ의 내면적 슬픔에는 극적인 감정선이 있는 곡이 깊게 스며들어요. ❄️"
    },
    ("ESTJ", "설렘"): {
        "songs": [
            ("EXO - LOVE SHOT", "It’s the love shot", "https://www.youtube.com/watch?v=pSudEWBAYRE"),
            ("방탄소년단 - 봄날", "보고 싶다, 보고 싶다", "https://www.youtube.com/watch?v=xEeFrLSkMm8"),
            ("레드벨벳 - 피카부", "피카부~ 새콤달콤해", "https://www.youtube.com/watch?v=6uJf2IT2Zh8")
        ],
        "reason": "설렘도 전략적으로 즐기는 ESTJ에겐 세련된 감성 팝이 잘 어울려요! ✨"
    },
    ("ENTJ", "지침"): {
        "songs": [
            ("이하이 - 한숨", "그대 고된 하루 끝에 한숨만 나와", "https://www.youtube.com/watch?v=gdZLi9oWNZg"),
            ("수란 - 오늘 취하면", "지친 오늘에 취하고 싶어", "https://www.youtube.com/watch?v=xZ8w5fscd5c"),
            ("크러쉬 - 소파", "그냥 소파에 기대어 혼자 있고 싶어", "https://www.youtube.com/watch?v=knt1y9L7sR8")
        ],
        "reason": "결단력 있는 ENTJ도 지칠 땐 따뜻한 위로가 필요하죠. 🪑"
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
