import streamlit as st

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 영화 추천기 🎬", page_icon="🎈", layout="centered")

# 🎉 헤더
st.title("🎬 MBTI 기반 명작 영화 추천기 💡")
st.subheader("MBTI를 선택하면 수학📐, 과학🧪 명작 영화가 짠!")
st.markdown("🎯 **심플하게 선택만 하면 끝!**")

# 🎬 MBTI별 영화 추천
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

# 👇 MBTI 선택 드롭다운
mbti = st.selectbox("🔍 당신의 MBTI를 선택해주세요:", options=sorted(movie_recommendations.keys()))

# 🎈 결과 출력
if mbti:
    st.balloons()
    st.success(f"🎉 {mbti} 유형에게 추천하는 영화는:")
    for movie in movie_recommendations[mbti]:
        st.markdown(f"- {movie}")
    st.markdown("🍿 팝콘 들고 감상 시작!")

