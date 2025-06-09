import streamlit as st

# 🎨 페이지 기본 설정
st.set_page_config(page_title="MBTI 영화 추천기 🎬", page_icon="🎈", layout="centered")

# 🎉 타이틀과 인트로
st.title("🎬 MBTI 기반 명작 영화 추천기 💡")
st.subheader("당신의 MBTI를 입력하면 과학🧪·수학📐 분야의 명작 영화를 추천해드릴게요!")
st.markdown("🧠 **개인 성향에 딱 맞는 과학적 명작을 만나보세요!**")

# 🎯 MBTI 입력 받기
mbti = st.text_input("📝 당신의 MBTI를 입력해주세요 (예: INTP)", max_chars=4).upper()

# 🎬 MBTI에 따른 영화 추천 사전
movie_recommendations = {
    "INTP": ["📽 인터스텔라 (Interstellar)", "🧠 굿 윌 헌팅 (Good Will Hunting)"],
    "INTJ": ["🧪 컨택트 (Arrival)", "🧬 프리퀀시 (Frequency)"],
    "ENTP": ["💥 마션 (The Martian)", "🔭 백 투 더 퓨처 (Back to the Future)"],
    "INFJ": ["🌀 인셉션 (Inception)", "⚛️ 테슬라 (Tesla)"],
    "ENFP": ["🧬 루시 (Lucy)", "🧪 페르마의 밀실 (The Fermat Room)"],
    "ISTJ": ["📐 뷰티풀 마인드 (A Beautiful Mind)", "🛰 그래비티 (Gravity)"],
    "ISFJ": ["🧪 히든 피겨스 (Hidden Figures)", "🌌 코스모스 (Cosmos)"],
    "ESTJ": ["🛰 아폴로 13 (Apollo 13)", "📡 컨택트 (Contact)"],
    "ESFJ": ["📚 페르마의 밀실 (The Fermat Room)", "💡 디스커버리 (The Discovery)"],
    "ENTJ": ["🚀 퍼스트 맨 (First Man)", "📊 스티브 잡스 (Steve Jobs)"],
    "ISTP": ["⚙ 테넷 (Tenet)", "🧠 트랜센던스 (Transcendence)"],
    "ISFP": ["🌱 트리 오브 라이프 (The Tree of Life)", "🧬 루시 (Lucy)"],
    "ESTP": ["🚗 백 투 더 퓨처 (Back to the Future)", "💡 스파크 (The Current War)"],
    "ESFP": ["🎉 빅 히어로 (Big Hero 6)", "🧠 인사이드 아웃 (Inside Out)"],
    "INFP": ["🌌 인터스텔라 (Interstellar)", "🧬 어라이벌 (Arrival)"],
    "ENFJ": ["🧠 굿 윌 헌팅 (Good Will Hunting)", "📈 디스커버리 (The Discovery)"],
}

# 🎈 추천 결과 표시
if mbti:
    if mbti in movie_recommendations:
        st.balloons()  # 풍선 효과 빵빵!
        st.success(f"🎉 {mbti} 유형에게 추천하는 영화는:")
        for movie in movie_recommendations[mbti]:
            st.markdown(f"- {movie}")
        st.markdown("🍿 팝콘 챙기고 즐감하세요!")
    else:
        st.warning("🤔 죄송해요! 아직 해당 MBTI에 대한 추천이 준비되지 않았어요.")
