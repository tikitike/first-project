# streamlit_rps_game.py
import streamlit as st
import random

# 이모지 세팅
choices = {
    "가위": "✂️",
    "바위": "🪨",
    "보": "🖐️"
}

# 결과 판정 함수
def get_result(user, computer):
    if user == computer:
        return "😐 무승부!"
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        return "🎉 당신이 이겼어요!"
    else:
        return "😭 컴퓨터가 이겼어요..."

# 제목
st.markdown("<h1 style='text-align: center;'>🎮 가위 ✂️ 바위 🪨 보 🖐️ 게임!</h1>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("## ✨ 아래에서 선택하세요!")

# 사용자 선택
user_choice = st.selectbox("당신의 선택은?", list(choices.keys()), index=0, format_func=lambda x: f"{choices[x]} {x}")

# 플레이 버튼
if st.button("🔫 대결!"):
    computer_choice = random.choice(list(choices.keys()))

    st.markdown("---")
    st.markdown(f"### 🧍‍♂️ 당신의 선택: {choices[user_choice]} **{user_choice}**")
    st.markdown(f"### 🤖 컴퓨터의 선택: {choices[computer_choice]} **{computer_choice}**")

    result = get_result(user_choice, computer_choice)
    st.markdown(f"## 🏁 결과: {result}")
    st.balloons() if "이겼어요" in result else st.snow() if "무승부" in result else None
