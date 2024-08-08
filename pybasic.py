import streamlit as st
import random   # 반드시 random을 먼저 실행하고 random 함수를 사용한다

#구구단 함수
def gugudan(): 
    dan = st.number_input("단입력>> ",value=1) 
    if dan >1:
        for i in range(1,10):
            multi = dan*i
            st.write(f" {dan} x {i} = {multi}")

# 음식추천 함수
def recommand_food(): 
    c_food = ['짜장면', '짬뽕', '탕수육', '팔보채', '유산슬']
    k_food = ['비빔밥', '갈비탕', '만두전골', '녹두전', '잡채']

    rc = st.radio("음식추천", ["중식", "한식"],index=None)
    if rc == "중식":
        st.write(f"오늘의 중식 추천메뉴: {random.choice(c_food)}")
    elif rc == "한식":
        st.write(f"오늘의 한식 추천메뉴: {random.choice(k_food)}")
    else:
        st.write(f"음식 종류를 선택하세요!")


def basic():
#탭 형식(다른 곳에 호출될 경우 반드시 함수로 만든다)
    tab1, tab2 = st.tabs(["구구단", "음식추천"])
    with tab1:
        gugudan()
    with tab2:
        recommand_food()
